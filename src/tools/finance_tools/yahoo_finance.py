"""
MCP Server to provide tools for financial data using Yahoo Finance API.

Note, right now, there's more logic in the tools than just retrieving the
information. Ideally, this logic is abstracted and the tools just provide a thin
interface to the underlying logic. This is hinted by the functionality provided
by ./finance_utils.py.

However, for demonstration purposes, we keep it this way - simple.
"""

import json
import yfinance as yf

from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field

from src.config.mcp_config import mcp_config
from src.tools.finance_tools.finance_utils import (
    get_stocks_in_s_and_p_500,
    fuzzy_search_ticker,
)


mcp = FastMCP("Yahoo Fiance Tools")


# EXAMPLE TOOL:
# In the following example, we define a tool to retrieve the stock price, given
# a ticker symbol. Besides the tool's logic, it's "interface" for the agent is
# of importance. Here, we utilize the tags to add metadata that can be used for
# searching the tool. This comes in handy when there is a plethora of tools
# available. Think about making a first selection according to read / write
# tools when accessing a database. The second specificity is the type annotation
# we are using for the functions parameters. While specifying the type, we use
# pydantic's functionality to check the parameter's validity and giving a more
# detailed description, which is important for an agent which uses the tool
# dynamically. We also emphasize that the field is required by using the ellipsis `...`.
@mcp.tool(tags={"finance", "read", "info"})
def get_stock_price(
    ticker: Annotated[
        str,
        Field(
            ...,
            description="The ticker identifying the stock. Search for it using the tool if it's not known to you.",
        ),
    ],
) -> str:
    """Get the current stock price for a given ticker symbol.

    Args:
        ticker: The ticker identifying the stock.

    Returns:
        A string stating the current stock price.
    """
    res: str = ""
    dat = yf.Ticker(ticker)
    current_price = dat.info.get("currentPrice", None)
    if current_price is not None:
        res = f"The current price of {ticker} is {current_price} USD."
    else:
        res = f"Sorry, I couldn't retrieve the price for ticker {ticker}."
    return res


@mcp.tool(tags={"finance", "read", "search"})
def search_stock_ticker(
    company_name: Annotated[
        str,
        Field(
            ...,
            description="The name of the company to search the ticker for.",
        ),
    ],
) -> str:
    """Fuzzy search for a stock ticker given a company name.

    Args:
        company_name: The name of the company to search the ticker for.

    Returns:
        JSON string containing info on possible matches, if found, otherwise a
        message indicating it wasn't found.
    """
    res: str = fuzzy_search_ticker(company_name)
    return res


@mcp.tool(tags={"finance", "read", "info"})
def get_full_stock_information(
    ticker: Annotated[
        str,
        Field(
            ...,
            description="The ticker identifying the stock. Search for it using the tool if it's not known to you.",
        ),
    ],
) -> str:
    """Get the full information about a stock given its ticker symbol.

    Args:
        ticker: The ticker identifying the stock.

    Returns:
        JSON string containing the full stock information available.
    """
    res: str = ""
    dat = yf.Ticker(ticker)
    info = dat.info
    res = json.dumps(info, indent=2)
    return res


@mcp.tool(tags={"finance", "read", "info", "s+p500", "stocks"})
def get_stocks_listed_in_s_and_p_500() -> str:
    """Get the list of stocks listed in the S&P 500 index.

    The data was obtained from kaggle with data from Q1 of 2025.
    Link: https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks

    Returns:
        A JSON string containing the list of stocks in the S&P 500 index.
    """
    stocks: dict = get_stocks_in_s_and_p_500()
    return json.dumps(stocks, indent=2)


if __name__ == "__main__":
    mcp.run(transport=mcp_config.transport_protocol, port=mcp_config.port)