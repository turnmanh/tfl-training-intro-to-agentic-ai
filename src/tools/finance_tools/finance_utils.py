import pandas as pd

from src.agents.text_extraction_agent import text_extraction_chain


def get_stocks_in_s_and_p_500() -> dict:
    """Get the list of stocks listed in the S&P 500 index.

    The data was obtained from kaggle with data from Q1 of 2025.
    Link: https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks

    Returns:
        A JSON containing the list of stocks in the S&P 500 index.
    """
    res: dict = {}
    # Read resource from disk.
    df: pd.DataFrame = pd.read_csv(
        "./src/tools/finance_tools/data/sp500_companies.csv", sep=","
    )

    # Example: transform the data a bit to yield a textual description.
    df = df.assign(
        description=df.apply(
            lambda row: f'{row["Shortname"]} is located in {row["City"]}, {row["State"]}',
            axis=1,
        )
    )

    # Convert to dictionary for easier JSON serialization to match the MIME type.
    res = df.groupby("Symbol")["description"].apply(list).to_dict()
    return res


def fuzzy_search_ticker(company_name: str, ticker: str | None = None) -> str:
    """Fuzzy search for a stock ticker given a company name.

    Args:
        company_name: The name of the company to search the ticker for.
        ticker: Optional known ticker to refine the search.

    Returns:
        The rows from the S&P 500 dataset that match the search criteria.
    """
    res: str = ""
    df: dict = get_stocks_in_s_and_p_500()

    if ticker:
        query = "Company name: " + company_name + ", or possible ticker: " + ticker
    else:
        query = "Company name: " + company_name

    # Perform a simple case-insensitive substring match.
    res = text_extraction_chain.invoke({"text": str(df), "query": query})

    return res
