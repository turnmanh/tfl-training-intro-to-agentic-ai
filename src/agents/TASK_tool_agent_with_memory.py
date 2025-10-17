import asyncio
import operator

from typing import Annotated, TypedDict
from langchain import hub
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph.graph.state import CompiledStateGraph
from langchain_mcp_adapters.tools import load_mcp_tools

# Note: tools are now provided async by a client.
from src.clients.llm_client import llm_client
from src.clients.mcp_client import mcp_client


# todo: create a checkpointer to create single checkpoints within a thread.


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

    # todo: adapt to include a checkpointer.
    graph_react_agent = create_react_agent(
        llm_client, tools
    )

    return graph_react_agent


async def stream_agent():
    """Async. streaming invocation of the agent with memory. """
    # MultiServerMCPClient is stateless by default. Each tool invocation creates
    # a fresh MCP ClientSession, executes the tool, and then cleans up. Thus,
    # one could also skip this step and get the tools via await
    # client.get_tools().
    async with mcp_client.session(server_name="yahoo_finance") as mcp_session:
        agent_graph = await create_react_agent_graph(mcp_session)

        # Provide a thread ID to maintain memory across calls. Within each
        # thread, the checkpointer will save the state after each invocation.
        # todo: create the required config to provide a thread id per execution.

        while True:
            user_input = input("User: ")
            # Allow to stop the loop via commands.
            if user_input.lower() in {"exit", "quit", "q"}:
                print("Exiting ...")
                break

            # Stream the agent's response.
            print("Agent: ", end="", flush=True)
            # todo: Provide the config with thread id to the astream call.
            async for message_chunk, _ in agent_graph.astream(
                {"messages": [HumanMessage(content=user_input)]},
                stream_mode="messages",
            ):
                if message_chunk.content and isinstance(message_chunk, AIMessage):  # type: ignore
                    print(message_chunk.content, end="", flush=True)
            print("\n")


async def invoke_agent():
    """Async. invocation of the agent with memory. """
    async with mcp_client.session(server_name="yahoo_finance") as mcp_session:
        agent_graph = await create_react_agent_graph(mcp_session)
        config: RunnableConfig = {"configurable": {"thread_id": 1}}

        while True:
            user_input = input("User: ")
            if user_input.lower() in {"exit", "quit", "q"}:
                print("Exiting ...")
                break

            # todo: Provide the config with thread id to the invocation call.
            result = await agent_graph.ainvoke(
                {"messages": [HumanMessage(content=user_input)]}
            )

            last_message = result["messages"][-1]
            if hasattr(last_message, "content"):
                print("Agent:", last_message.content)
            print()


if __name__ == "__main__":
    asyncio.run(invoke_agent())
