"""
This module implements a ReAct (Reasoning and Acting) agent using LangGraph.

The ReAct pattern allows the agent to:
1. Reason about a user's request
2. Decide if it needs to use external tools to gather information
3. Execute those tools
4. Reason again based on the tool outputs
5. Formulate a final response

Key components:
- StateGraph: Defines the flow of the agent
- Agent Node: The LLM processing step
- Tool Node: Executes selected tools
- Conditional Logic: Determines whether to loop back to tools or finish
"""


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


# Compile the graph into an executable app.
app = flow.compile()


def stream_react_agent():
    """Run the agent graph in a loop."""
    state: State = {"messages": []}

    while True:
        user_input = input("User: ")
        # Allow to stop the loop via commands.
        if user_input.lower() in {"exit", "quit", "q"}:
            print("Exiting...")
            break

        state["messages"].append(HumanMessage(content=user_input))
        for msg_chunk, _ in app.stream(state, stream_mode="messages"):  # type: ignore
            if msg_chunk.content and isinstance(msg_chunk, AIMessage):  # type: ignore
                print(msg_chunk.content, end="|", flush=True)
        print("\n")


def invoke_react_agent():
    """Run the agent graph in a loop."""
    state: State = {"messages": []}

    while True:
        user_input = input("User: ")
        # Allow to stop the loop via commands.
        if user_input.lower() in {"exit", "quit", "q"}:
            print("Exiting...")
            break

        state["messages"].append(HumanMessage(content=user_input))
        result = app.invoke(state)
       
        last_message = result["messages"][-1]
        if isinstance(last_message, AIMessage) and last_message.content:
            print(last_message.content)  # type: ignore
        print()


if __name__ == "__main__":
    invoke_react_agent()
