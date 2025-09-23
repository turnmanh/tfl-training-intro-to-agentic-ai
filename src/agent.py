import operator

from typing import Annotated, TypedDict
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END, START

from src.clients.llm_client import llm_client
from src.tools import tools


# Bind the tools to the LLM client.
llm_client_with_tools = llm_client.bind_tools(tools)


# Initialize the tool node that looks for tool_calls within the messages.
tool_node = ToolNode(tools)


class State(TypedDict):
    """State of the agent."""
    messages: Annotated[list[BaseMessage], operator.add]


def continue_tool_calls(state: State) -> str:
    """Determine whether to continue tool calls based on the state."""
    res: str = ""
    last_message: AIMessage = state["messages"][-1]  # type: ignore

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        res = "continue"
    else:
        res = "stop"

    return res


def invoke_agent(state: State) -> dict:
    """Invoke the agent with the given state."""
    messages = state["messages"]
    response: BaseMessage = llm_client_with_tools.invoke(messages)
    return {"messages": [response]}


# Construct the graph.
flow = StateGraph(State)

# Add the central nodes of an agentic system.
flow.add_node("agent", invoke_agent)
flow.add_node("tool_node", tool_node)

# Now, connect the nodes together using edges.
# Set the entrypoint of the system. There are two ways to do this:
# flow.add_edge(START, "agent")
flow.set_entry_point("agent")
# Add the conditional edge. The graph will call `continue_tool_calls` AFTER the
# `agent` node is executed. Based on the string output, it will route to "tools"
# or to the special END node.
flow.add_conditional_edges(
    "agent",
    continue_tool_calls,
    {
        "continue": "tool_node",
        "stop": END,
    },
)
flow.add_edge("tool_node", "agent")

app = flow.compile()
