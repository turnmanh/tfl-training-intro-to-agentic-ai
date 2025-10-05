# Yahoo Finance MCP Server 

## Inspection 

To inspect the server and its tools, you can use the [MCP
Inspector](https://github.com/modelcontextprotocol/inspector). This tool allows
to list and call all tools, prompts, and resources provided by the MCP server. 

```bash
npx @modelcontextprotocol/inspector
```

## Execution

There are several options to run the server. First, we've followed standard
practices and included a `if __name__ == "__main__":` block at the end of the
module. This allows you to run the server directly by executing the module with
Python. The special configurations of the server are provided in the `run()`
method.

Alternatively, you can use the CLI provided by FastMCP. This does not execute
the __main__ block, but instead imports the server object and runs it with the
configurations provided in the CLI.

```bash
fastmcp run yahoo_finance.py:mcp --transport <TRANSPORT> --port <PORT>
```

Or in this specific case:

```bash
uv run fastmcp run src/tools/finance_tools/yahoo_finance.py:mcp --transport http --port 9090
```

## Calling the Server

Irrespective of how the server is run, it can be accessed using a FastMCP
client. FastMCP clients are asynchronous and therefore require an async context.

```python
import asyncio
from fastmcp import Client

client = Client("<ENDPOINT>")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("<TOOL-NAME>", {"<PARAMETER>": <VALUE>})
```

The LangChain ecosystem provides [several
adapters](https://github.com/langchain-ai/langchain-mcp-adapters) to use MCP
servers as tool providers. 
