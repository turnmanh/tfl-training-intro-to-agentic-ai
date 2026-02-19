import operator

from typing import Annotated, TypedDict
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END
from pydantic import BaseModel, Field

from src.clients.llm_client import llm_client
from src.tools import tools


# Bind the tools to the LLM client.
llm_client_with_tools = llm_client.bind_tools(tools)


# Initialize the tool node that looks for tool_calls within the messages.
tool_node = ToolNode(tools)


class Plan(BaseModel):
    """A plan consisting of steps to accomplish a task."""

    steps: list[str] = Field(
        description="A list of steps to accomplish the task. Should be in order."
    )


# --- State Definition ---


class State(TypedDict):
    """State of the plan-and-execute agent."""

    input: str
    plan: list[str]
    past_steps: Annotated[list[tuple[str, str]], operator.add]
    response: str
    messages: Annotated[list[BaseMessage], operator.add]


# --- Node Functions ---


def planner(state: State) -> dict:
    """Create a plan to accomplish the task."""
    planner_prompt = SystemMessage(
        content="""You are a planner. Given a user request, create a step-by-step plan to accomplish the task.

Rules:
- Maximum 5 steps
- Each step should be a short, high-level action (max 10 words)
- Do not include detailed instructions or measurements
- Focus on the key milestones, not every sub-task"""
    )

    planner_llm = llm_client.with_structured_output(Plan)
    plan: Plan = planner_llm.invoke(
        [planner_prompt, HumanMessage(content=state["input"])]
    )  # type: ignore

    print(f"\nGenerated Plan: {plan.steps}")

    return {"plan": plan.steps}


def executor(state: State) -> dict:
    """Execute the current step of the plan."""
    current_step = state["plan"][0]

    executor_prompt = SystemMessage(
        content=f"""You are an executor. Execute the following step using available tools if needed.

Current step to execute: {current_step}

Original task: {state['input']}

Previous steps completed:
{chr(10).join([f"- {step}: {result}" for step, result in state['past_steps']]) if state['past_steps'] else "None"}

Execute this step and provide a clear result."""
    )

    # Start fresh messages for this execution step
    messages = [executor_prompt, HumanMessage(content=f"Execute: {current_step}")]
    response: BaseMessage = llm_client_with_tools.invoke(messages)

    return {
        "messages": [
            executor_prompt,
            HumanMessage(content=f"Execute: {current_step}"),
            response,
        ]
    }


def continue_tool_calls(state: State) -> str:
    """Determine whether to continue tool calls based on the state."""
    last_message: AIMessage = state["messages"][-1]  # type: ignore

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "continue"
    return "stop"


def process_tool_result(state: State) -> dict:
    """Process the result after tool execution and update past_steps."""
    current_step = state["plan"][0]

    # Get the last AI message content as the result.
    last_ai_message = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, AIMessage) and msg.content:
            last_ai_message = msg
            break

    result = last_ai_message.content if last_ai_message else "Step completed"

    # Update plan by removing the completed step.
    remaining_plan = state["plan"][1:]

    return {
        "past_steps": [(current_step, str(result))],
        "plan": remaining_plan,
        "messages": [],  # Clear messages for next step.
    }


def replanner(state: State) -> dict:
    """Replan based on results so far, or finalize if done."""
    replanner_prompt = SystemMessage(
        content="""You are a replanner. Based on the original task and the steps completed so far,
decide if the plan needs adjustment or if the task is complete.

Rules:
- If the original task is accomplished, return an empty plan.
- If there are still steps to do, return the remaining steps in order.
- Add new steps if necessary, but keep the plan concise (max 5 steps total).
- Be as efficient as possible and avoid unnecessary steps.
"""
    )

    context = f"""Original task: {state['input']}

Steps completed:
{chr(10).join([f"- {step}: {result}" for step, result in state['past_steps']])}

Remaining plan:
{chr(10).join([f"- {step}" for step in state['plan']]) if state['plan'] else "None"}

Should we continue with the current plan, adjust it, or is the task complete?"""

    replanner_llm = llm_client.with_structured_output(Plan)
    new_plan: Plan = replanner_llm.invoke(
        [replanner_prompt, HumanMessage(content=context)]
    )  # type: ignore

    return {"plan": new_plan.steps}


def responder(state: State) -> dict:
    """Generate the final response based on all completed steps."""
    responder_prompt = SystemMessage(
        content="""You are a responder. Based on the original task and all the steps that were executed,
provide a comprehensive final response to the user."""
    )

    context = f"""Original task: {state['input']}

All steps completed:
{chr(10).join([f"- {step}: {result}" for step, result in state['past_steps']])}

Provide a final, helpful response to the user based on the above."""

    response: AIMessage = llm_client.invoke(
        [responder_prompt, HumanMessage(content=context)]
    )  # type: ignore

    return {"response": response.content}


# --- Routing Functions ---


def should_continue_plan(state: State) -> str:
    """Determine if we should continue executing the plan or finish."""
    if state["plan"]:
        return "continue"
    return "finish"


# --- Construct the Graph ---

flow = StateGraph(State)


# Add nodes.
flow.add_node("planner", planner)
flow.add_node("executor", executor)
flow.add_node("tool_node", tool_node)
flow.add_node("process_result", process_tool_result)
flow.add_node("replanner", replanner)
flow.add_node("responder", responder)


# Set entry point.
flow.set_entry_point("planner")


# Add edges.
flow.add_edge("planner", "executor")

# After executor, check if tools need to be called.
flow.add_conditional_edges(
    "executor",
    continue_tool_calls,
    {
        "continue": "tool_node",
        "stop": "process_result",
    },
)

# Tool node loops back to executor for potential additional tool calls.
flow.add_edge("tool_node", "executor")

# After processing result, go to replanner.
flow.add_edge("process_result", "replanner")

# After replanning, decide to continue or finish.
flow.add_conditional_edges(
    "replanner",
    should_continue_plan,
    {
        "continue": "executor",
        "finish": "responder",
    },
)

# Responder ends the flow
flow.add_edge("responder", END)


# Compile the graph into an executable app.
app = flow.compile()


def invoke_plan_and_execute_agent():
    """Run the plan-and-execute agent."""
    while True:
        user_input = input("User: ")
        # Allow to stop the loop via commands.
        if user_input.lower() in {"exit", "quit", "q"}:
            print("Exiting...")
            break

        initial_state: State = {
            "input": user_input,
            "plan": [],
            "past_steps": [],
            "response": "",
            "messages": [],
        }

        print("\n--- Planning ---")
        result = app.invoke(initial_state)

        print("\n--- Final Response ---")
        print(result["response"])
        print()


def stream_plan_and_execute_agent():
    """Run the plan-and-execute agent with streaming updates."""
    while True:
        user_input = input("User: ")
        # Allow to stop the loop via commands.
        if user_input.lower() in {"exit", "quit", "q"}:
            print("Exiting...")
            break

        initial_state: State = {
            "input": user_input,
            "plan": [],
            "past_steps": [],
            "response": "",
            "messages": [],
        }

        print("\n--- Executing Plan ---")
        for state_update in app.stream(initial_state):
            node_name = list(state_update.keys())[0]
            node_state = state_update[node_name]

            if node_name == "planner" and "plan" in node_state:
                print(f"\nPlan created:")
                for i, step in enumerate(node_state["plan"], 1):
                    print(f"  {i}. {step}")

            elif node_name == "process_result" and "past_steps" in node_state:
                step, result = node_state["past_steps"][0]
                print(f"\n✓ Completed: {step}")
                print(f"  Result: {result[:200]}...")  # Truncate long results

            elif node_name == "responder" and "response" in node_state:
                print(f"\n--- Final Response ---")
                print(node_state["response"])

        print()


if __name__ == "__main__":
    stream_plan_and_execute_agent()
