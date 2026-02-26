---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Providing Toolboxes for Agents 🧰
  </div>
</div>


---
title: Tool Engineering
subtitle: Critical Component
---

::grid{columns=2 gap=md width=100}
:::box{color=grey}
**Tools are central to most agentic systems**

They deserve as much attention as your prompts ‼️
:::

:::box{color=blue }
**How Tools Work**

Enable LLMs to interact with external services/APIs through specified structure
and definition, usually RPCs.

Capable models include tool use blocks in API response when planning to invoke a tool.
:::
::

<br>

**Example Tool Call Request**

```txt
User: what's the weather like in munich?
...

Tool Calls: [{'name': 'forecast_weather', 'args': {'location': 'munich'}, 'id': 'a01bd898-4dd7-4095-a87b-ca0aacda5fd2', 'type': 'tool_call'}]
...

The weather forecast for munich is [...]
```


---
title: Tool Format
subtitle: Key Suggestions
---

::grid{columns=1 gap=lg width=90}
:::box{color=white text=md}
**1. Give the model thinking space**

Enough tokens to "think" before writing itself into a corner
:::

:::box{color=blue text=md}
**2. Keep format natural**

Close to what model has seen on the internet
:::

:::box{color=dark-blue text=md}
**3. Minimize formatting overhead**

No accurate counting of thousands of lines, no string-escaping code
:::
::

---
title: Agent-Computer Interface (ACI)
subtitle: Design Principles
align: center
---

::grid{columns=1 width=80}
:::box{color=grey text=lg}
**💡 Rule of Thumb:**

Invest as much effort in ACI as you would in HCI (Human-Computer Interface)
:::
::

:vspace{size=lg}


---
title: Tool Documentation
subtitle: Best Practices
---

::grid{columns=1 gap=sm width=90}
:::box{color=blue text=sm}
**🤔 Put yourself in the model's shoes**

Is it obvious how to use this tool from description and parameters?
:::

:::box{color=white text=sm}
**📝 Write like for a junior developer**

Clear parameter names, comprehensive descriptions
:::

:::box{color=dark-blue text=sm}
**📚 Include essential details**

Example usage, edge cases, input format requirements, boundaries from other tools
:::

:::box{color=grey text=sm}
**⚠️ Especially important with similar tools**

Make distinctions clear
:::
::

---
title: Tool Testing & Iteration
---

::grid{columns=1 gap=lg width=90}
:::box{color=blue text=md}
**🧪 Test extensively**

Run many example inputs in workbench, see what mistakes the model makes
:::

:::box{color=white text=md}
**🔄 Iterate based on findings**

Adjust based on observed errors
:::

:::box{color=dark-blue text=md}
**🛡️ Poka-yoke your tools**

Change arguments to make mistakes harder (error-proofing)
:::
::


---
title: Some Examples for Standardized Tooling
---

::grid{columns=3 width=100 gap=md}

<v-click>

:::field{align=end span=1}
::::imgx{src=./sections/shared_images/logo_atlassian.png}
MCP-Atlassian
::::
:::

</v-click>
<v-click>

:::field{align=end span=1}
::::imgx{src=./sections/shared_images/logo_playwright.svg}
Playwright MCP
::::
:::

</v-click>
<v-click>

:::field{align=end span=1}
::::imgx{src=./sections/shared_images/logo_mcp_registry.png}
MCP Registry
::::
:::

</v-click>

::


---
title: Every day more tools are being standardized and shared 
---

::grid{columns=2 width=100 gap=md}

:::field{align=top span=1}
::::imgx{src=./sections/shared_images/ucp_banner.jpeg width=90}
Universal Connector Protocol (UCP)
::::
:::

<v-click>

:::field{align=top span=1}
HTML with WebMCP Annotations
```html
<form 
  action="/search" 
  method="POST"
  **tool-name="search_flights"** **tool-description="Search for available flights based on origin and date"**
  **tool-autosubmit**>
    <input name="origin" type="text" placeholder="From...">
    <input name="departure_date" type="date">
    <button type="submit">Search</button>
</form>
```

Standard HTML
```html
<form action="/search" method="POST">
    <input name="origin" type="text" placeholder="From...">
    <input name="departure_date" type="date">
    <button type="submit">Search</button>
</form>
```

:::

</v-click>

::


---
title: Model Context Protocol for Reference
---

::imgx{src=./sections/shared_images/mcp.png width=90}
Illustration of MCP Components. Illustration from LangChain.
::


---
title: Discussion
---

:::box{color=white text=lg}

**⁉️**

<hr
style="
height: 3px;
background-color: #d6dde0ff;
margin-top: 0.5rem;
margin-bottom: 1rem;
">

In your personal / work live. What functionality would you **package and
provide** in form of an external server?

:::


---
title: Developing MCP Servers
---

Have a look into modules at `src/tools/finance_tools` for reference.

```python
mcp = FastMCP("Yahoo Finance Tools")
...

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
```


---
title: Developing MCP Servers
---

Have a look into modules at `src/tools/finance_tools` for reference.

```python
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
        ...
        ...
```


---
title: Automatic Validation and Casting of Parameters 
---

MCP provides data parsing and validation. 

Given: 
```python
@jira_mcp.tool(tags={"jira", "read"})
async def get_issue(
    ctx: Context,
    issue_key: ...,
    ...
```

The agent's input is parsed via **dictionary unpacking** and type checked using
Pydantic. Note: Context is injected automatically.

```python
get_issue(ctx=Context, **llm_params)
```


--- 
title: Inspecting MCP Servers
---

Inspect tools, prompts, resources etc. provided by a MCP server via:

```bash
npx @modelcontextprotocol/inspector
```


---
title: Extending the Tool Use Agent with More Tools ⌨️
text: lg
align: center
---

1. Open the file `src/tools/TASK.md` and read the description of the **second** (2️⃣) task.
2. Implement more tools for the MCP server by adding them in `src/tools/finance_tools/yahoo_finance.py` as needed. Feel free to
   implemented the suggested tools or create your own.
3. Interact with your agent by running it as
    ```bash
    uv run python -m src.agents.tool_agent
    ```

<br>
<br>

<v-click>

::box{align=center text=lg color=dark-blue}
🔬 Feel free to try models of different complexities, e.g., gpt-5, mini, and nano.
::

</v-click>


---
title: What have you built? What have you learned?
text: lg
align: center
---

Feel free to share your agents! 🚀 <v-click> ... and then we can grab a **coffee**! ☕️ </v-click>