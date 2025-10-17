---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Keeping Track of the Past 💾
  </div>
</div>


---
title: Memory in Agents
---

::::imgx{src=./sections/shared_images/memory_short_vs_long.png}
Illustration of Memory in Agentic Systems. Illustration by LangChain.
::::


---
title: Managing Short Term Memory
align: center
---

::grid{cols=5 width=100 gap=md}

:::box{align=center span=2}
**Considerations**
- How many messages to keep in context?
- Which messages to keep in context?
- How to prevent noise from irrelevant messages?
- ...
:::

:::field{span=3}
::::imgx{src=./sections/shared_images/memory_filtering_long_thread.png}
Illustration of Filtering Short Term Management. Illustration from LangChain.
:::

::

---
title: Memory Types according to CoALA
---

| Memory Type  | What is Stored | Human Example | Agent Example |
|--------------|----------------|---------------|---------------|
| _Semantic_  | Facts  | Things I learned in school   | Facts about a user   |
| _Episodic_    | Experiences   | Things I did                 | Past agent actions   |
| _Procedural_  | Instructions  | Instincts or motor skills    | Agent system prompt  |


---
title: Semantic Memory
subtitle: Long-term Memory
---

::grid{cols=5 width=90}

:::box{color=white span=3 align=center}
- Information learned in school and the understanding of concepts and their
relationships.
- Used to personalize applications by remembering facts or concepts.
- Organization e.g. in profiles or collections.
:::

:::field{span=2}
::::imgx{src=./sections/shared_images/long_term_memory_semantic.png}
Illustration of Semantic Memory. Illustration from LangChain.
::::
:::
::


---
title: Episodic Memory
subtitle: Long-term Memory
---

- Recalling past events or actions.
- Facts can be written to semantic memory, whereas experiences can be written to episodic memory.
- Few-shot examples or summaries of past interactions.
- Showing / telling, i.e., describing, can be easier than programming.


---
title: Procedural Memory
subtitle: Long-term Memory
---

::grid{cols=5 width=90}

:::box{color=white span=3 align=center}
- Remembering the rules used to perform tasks.
- Combination of model weights, agent code, and agent’s prompt that collectively determine the agent’s functionality.
- Agents can modify their prompts based on experiences, e.g., via _reflection_.
:::

:::field{span=2}
::::imgx{src=./sections/shared_images/long_term_memory_procedural.png}
Illustration of Procedural Memory. Illustration from LangChain.
::::
:::
::



---
title: Updating Strategies for Memory
---

::grid{cols=5 width=90}

:::box{color=white span=3 align=center}
- Real-time vs. Latency and Quality
- Transparency vs. Redundancy
- See [memory-agent](https://github.com/langchain-ai/memory-agent) for _in the
  hot path_ example.
- See [memory-service](https://github.com/langchain-ai/memory-template) for _in
  the background_ example.
:::

:::field{span=2}
::::imgx{src=./sections/shared_images/memory_updating_strategies.png}
Illustration of Updating Long-term Memory. Illustration from LangChain.
::::
:::
::


---
title: Extending the ReAct Agent with More Tools ⌨️
text: lg
align: center
---

1. Open the file `src/agents/TASK_tool_agent_with_memory.md` and add thread memory.
2. Think about how to add a filtering mechanism to keep the context relevant.

<br>
<br>

<v-click>

::box{align=center text=lg color=dark-blue}
🔬 Feel free to try models of different complexities, e.g., gpt-5, mini, and nano.
::

</v-click>

