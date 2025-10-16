---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Reasoning and Acting Agent 🤖
  </div>
</div>


---
title: ReAct Agent
---

::grid{cols=2 width=100 gap=md}

:::box{color=blue align=center span=1 height=40}

- **Thought** -- reasoning about situation and what to do
- **Action** -- calls a tool, searches, etc.
- **Observation** -- observation of a result
- **Repeat** -- loop until task is complete

:::

:::field{color=dark-blue text=md span=1 height=40}
::::imgx{src=./sections/shared_images/illustration_react.svg}
Illustration of the ReAct agent framework.
:::

::


---
title: Some More Popular Agentic Architectures
---

::grid{cols=3 width=100 gap=sm}

<!-- Row one. -->
:::box{color=blue align=top span=1 height=40 text=sm}

**Tree of Thoughts** (ToT)

- Explores multiple paths simultaneously (breadth-first/depth-first)
- Good for: Complex problems with multiple solution approaches
- Downside: Computationally expensive
:::

:::box{color=dark-blue align=top span=1 height=40 text=sm}

**Chain of Thought** (CoT)

- Linear step-by-step reasoning
- Simple, effective for straightforward logical tasks
- Can be zero-shot ("let's think step by step") or few-shot (with examples)
:::

:::box{color=grey align=top span=1 height=40 text=sm}

**Reflexion**

- Agent reflects on its own outputs/failures
- Uses self-evaluation to improve next iteration
- Good for: Iterative refinement tasks (coding, writing)
:::

<!-- Row two. -->
:::box{color=white align=top span=1 height=40 text=sm}

**Plan-and-Execute**

- Creates full plan upfront, then executes sequentially
- Can re-plan if execution fails
- Good for: Well-defined workflows with clear steps
:::

:::box{color=grey align=top span=1 height=40 text=sm}

**Multi-Agent Systems**

- Multiple specialized agents collaborate
- Can debate, delegate, or work in parallel
- Examples: AutoGen, CrewAI patterns
:::

:::box{color=dark-blue align=top span=1 height=40 text=sm}

**Graph-Based** (LangGraph style)

- Explicit state machines with defined transitions
- Conditional routing between nodes
- Good for: Complex workflows needing precise control
:::

::


---
title: Building a ReAct Agent with LangGraph
---

::grid{cols=2 width=100 gap=md}

:::box{color=white align=center span=1 height=50}
- Graph structure as **nodes and edges**
- Nodes perform specific functions (e.g., LLM call, tool call, etc.)
- A graph has an **entrypoint and an exit point**
- Edges define the flow of data between nodes
- LangGraph supports **state management**, allowing nodes to read from and write to a shared state
:::

:::box{color=grey span=1 height=50 align=center}
```python
# Construct the graph.
flow = StateGraph(State)
...

flow.set_entry_point("agent")
...

flow.add_edge("tool_node", "agent")
```
::: 
::


---
title: Tools are Decorated Functions
---

::grid{cols=10 width=100}

:::box{color=blue align=center span=6 height=60}
```python
@tool
def forecast_weather(location: str) -> str:
    """Get the weather forecast for a given location.
    
    Args:
        location: The location to get the weather forecast for.
    
    Returns:
        A string describing the weather forecast.
    """
```
:::

:::box{color=dark-blue align=center span=4 height=60} 
⚠️ It's important to provide a **clear and concise docstring** for each tool, as
this is what the agent will use to understand how to use the tool. 
:::

::


---
title: Creating Your First ReAct Agent ⌨
text: lg
align: center
---

1. Open the `src/agents/TASK_react_agent.py` file. You will find several `todo` comments indicating where you need to add code.
2. Follow the instructions in the comments to implement the ReAct agent.
3. Once you have completed the implementation, run the script to see your agent in action!
    ```python
    uv run python -m src.agents.TASK_react_agent
    ``` 


---
title: Extending the ReAct Agent with More Tools ⌨️
text: lg
align: center
---

1. Open the file `src/tools/TASK.md` and read the description of the **first** task.
2. Implement more tools in the `src/tools` directory as needed. Feel free to
   implemented the suggested tools or create your own.


---
title: What have you built? What have you learned?
text: lg
align: center
---

Feel free to share your agents! 🚀 <v-click> ... and then we can go into the
lunch break! 🍽️ </v-click>


