from langchain_mcp_adapters.client import MultiServerMCPClient


mcp_client = MultiServerMCPClient(
    {
        "yahoo_finance": {
            "url": "http://localhost:9090/mcp",
            "transport": "streamable_http"
        }
    }
)
