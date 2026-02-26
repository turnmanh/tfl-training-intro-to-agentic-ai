---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Reasoning and Acting Agent 🤖
  </div>
</div>


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

1. Open the file `src/tools/TASK.md` and read the description of the **first**
   (1️⃣) task.
2. Implement more tools in the `src/tools` directory as needed. Feel free to
   implemented the suggested tools or create your own.

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

Feel free to share your agents! 🚀 <v-click> ... and then we can go into the
**lunch** break! 🍽️ </v-click>


