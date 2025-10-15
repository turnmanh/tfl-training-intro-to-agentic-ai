# Task: Tool Creation 

We have outlined the tasks on writing tools for the agent. In general, tools
serve as external functions that the agent can call to perform specific actions
with - so called **actuators**.

They can also be helpful to break down complex problems into smaller, more
manageable and provide specific functionalities that the agent can leverage to
achieve its goals. E.g., instead of using a complex web interface, the agent can
call simple, well-defined functions to perform specific tasks. This mitigates
any confusions that may arise from the complexity of the web interface and thus,
requiring lots of tokens.

## Task 1 - Writing regular tools 

You can find a sample tool in `./weather_tools.py`, which is essentially just a
placeholder as it cannot do anything useful up to now. The tool itself is
provided to the agent via the list of `tools`, created in `./__init__.py`.

⚠️ Your **task** is to implement a useful tool that can be used by the agent.
Feel free to tackle any problem you like, not necessarily related to weather. 

In case you don't know where to start, here are some ideas:
- A tool for integer calculations (e.g., addition, subtraction, multiplication,
  division)
- A tool for unit conversions (e.g., kilometers to miles, Celsius to Fahrenheit)
- A tool for date and time manipulations (e.g., calculating the difference
  between two dates, adding days to a date)
- ...
- And if you're curious, write a tool for searching the web (e.g., using a search engine API s.a. tavily)

## Task 2 - Adding tools to a toolkit 

We've provided a sample toolkit as MCP server in `./finance_tools/`. The server
provides several tools to the agent, allowing it to fetch stock prices and
other financial data.

⚠️ Your **task** is to add another tool to the server. You can either implement
a completely new tool or add another tool from the existing [Yahoo Finance
API](https://ranaroussi.github.io/yfinance/). Make sure to separate the tool and
the logic required s.t. the tool can be as lean as possible.

💡 Make sure to provide well-written docstrings to the agent and incorporate
type hints as much as possible. You've also learned about the use of pydantic to
validate parameters. Finally, feel free to capitalize on the fact that the MCP
can automatically parse the data. 

In case you don't know where to start, here are some ideas:
- The [200-day simple moving average](https://www.investopedia.com/ask/answers/013015/why-200-simple-moving-average-sma-so-common-traders-and-analysts.asp#:~:text=Key%20Takeaways-,The%20200%2Dday%20simple%20moving%20average%20(SMA)%20is%20a,potential%20support%20or%20resistance%20levels.) (SMA) for a given stock ticker
- A variable X-day simple moving average for a given stock ticker, allowing to
  incorporate the 50-day SMA as well. 
- Find relatively "undervalued" stocks based on the [price-to-earnings
  ratio](https://www.investopedia.com/terms/p/price-earningsratio.asp)
