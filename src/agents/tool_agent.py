"""
This module implements a basic tool-enabled agent using LangGraph.

The tool agent provides:
1. Dynamic tool loading from an MCP (Model Context Protocol) server
2. A pre-built ReAct agent pattern for tool invocation
3. Streaming response output for real-time interaction
4. Stateless operation (no memory between conversations)

Key components:
- MCP Client: Connects to external tool servers
- load_mcp_tools: Dynamically loads available tools from MCP
- create_react_agent: Pre-built agent factory from LangChain
- Streaming: Real-time token-by-token response output
"""


import asyncio
import operator

from typing import Annotated, TypedDict
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain.agents import create_agent as create_react_agent
from langgraph.graph.state import CompiledStateGraph
from langchain_mcp_adapters.tools import load_mcp_tools

# Note: tools are now provided async by a client.
from src.clients.llm_client import llm_client
from src.clients.mcp_client import mcp_client


class State(TypedDict):
    """State of the agent."""

    messages: Annotated[list[BaseMessage], operator.add]


async def create_react_agent_graph(mcp_session) -> CompiledStateGraph:
    """Create a React agent graph with tools.

    Args:
        mcp_session: An active MCP client session.

    Returns:
        A StateGraph representing the agent flow.
    """
    tools: list = []
    resources: list = []

    # Load tools from the MCP server.
    tools_mcp = await load_mcp_tools(mcp_session)
    tools.extend(tools_mcp)

    graph_react_agent = create_react_agent(
        llm_client,
        tools,  # prompt=agent_prompt,
    )

    return graph_react_agent


async def stream_agent():
    """Async. streaming invocation of the agent with memory."""
    # MultiServerMCPClient is stateless by default. Each tool invocation creates
    # a fresh MCP ClientSession, executes the tool, and then cleans up. Thus,
    # one could also skip this step and get the tools via await
    # client.get_tools().
    async with mcp_client.session(server_name="yahoo_finance") as mcp_session:
        agent_graph = await create_react_agent_graph(mcp_session)

        while True:
            user_input = input("User: ")
            # Allow to stop the loop via commands.
            if user_input.lower() in {"exit", "quit", "q"}:
                print("Exiting ...")
                break

            # Stream the agent's response.
            print("Agent: ", end="", flush=True)
            async for message_chunk, _ in agent_graph.astream(
                {"messages": [HumanMessage(content=user_input)]},
                stream_mode="messages",
            ):
                if message_chunk.content and isinstance(message_chunk, AIMessage):  # type: ignore
                    print(message_chunk.content, end="", flush=True)
            print("\n")


async def invoke_agent():
    """Async. invocation of the agent with memory."""
    async with mcp_client.session(server_name="yahoo_finance") as mcp_session:
        agent_graph = await create_react_agent_graph(mcp_session)

        while True:
            user_input = input("User: ")
            if user_input.lower() in {"exit", "quit", "q"}:
                print("Exiting ...")
                break

            result = await agent_graph.ainvoke(
                {"messages": [HumanMessage(content=user_input)]},
            )

            last_message = result["messages"][-1]
            if hasattr(last_message, "content"):
                print("Agent:", last_message.content)
            print()


if __name__ == "__main__":
    asyncio.run(invoke_agent())
