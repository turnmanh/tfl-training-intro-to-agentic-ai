from typing import Literal
from pydantic import BaseModel, Field


class MCPConfig(BaseModel):
    """Configuration for the MCP server.

    Attributes:
        host: The host to bind the server to.
        transport_protocol: The protocol to use.
        port: The port to bind the server to.
    """

    host: str = Field(
        description="The host to bind the MCP server to.", default="127.0.0.1"
    )
    transport_protocol: Literal["stdio", "http", "sse", "streamable-http"] = Field(
        description="The protocol to use.", default="http"
    )
    port: int = Field(description="The port to bind the MCP server to.", default=9090)


mcp_config = MCPConfig()
