---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Introduction to Agentic Systems
  </div>
</div>


---
title: The Transition from "AI that Helps" to "AI that Does"
---

::grid{columns=2 width=100}
:::box{align=top justify=left}
Previously: **AI that helps**
- Improved tooling
- Autocomplete for emails
- Suggestions in your IDE
- Insights from your data
- "Would you like me to draft that?"
:::

:::box{align=top justify=left}
Now / Coming: **AI that does**
- Agents that complete multi-step workflows
- Systems make decisions within defined parameters
- AI maintains context within set scopes
- Software coordinates with other software
:::
::

<br>

<v-click>

:::box{color=dark-blue span=3 height=10} 
2024-2025 marks the transition from "AI that helps" to "AI that does."
Understanding this shift determines who employs agents successfully. 
:::

</v-click>

<br>

<v-click>

:::box{color=blue span=3 height=10 color=white}
_"Nearly eight in ten companies report using gen AI—yet just as many report no
significant bottom-line impact."_, McKinsey, March 2025
:::

</v-click>


---
title: Process Characteristics Suitable for Agent Employment
---

::grid{columns=4 width=100 gap=md}
:::box{height=40 align=top justify=left text=md color="dark-blue"}
**High Coordination Effort**

 - Multiples systems
 - Context switching
 - Manual data aggregation

:::

<v-click>

:::box{align=top justify=left text=md color="dark-blue"}
**Ambiguity**

 - Judgment on incomplete data
 - Unstructured inputs
 - Exceptions that don't fit rigid rules

:::

</v-click>

<v-click>

:::box{align=top justify=left text=md color="dark-blue"}
**Dynamic Environment**

 - Intermediate results determine path
 - Iterative refinement 

:::

</v-click>

<v-click>

:::box{align=top justify=left text=md color="dark-blue"}
**Knowledge-intensive Operations**

 - Requires synthesis of information
 - Domain expertise at scale

:::

</v-click>

::

<br>

<v-click>

::box{height=30 align=center justify=left color=grey}
**❌ Where they don't fit** 

 - High-volume tasks
 - Deterministic paths
 - Safety-critical operations

::

</v-click>


---
title: Discussion
---

:::box{color=white text=lg}

**⁉️**

<hr
style="
height: 3px;
background-color: #d6dde0ff;
margin-top: 0.5rem;
margin-bottom: 1rem;
">

Where can you see agentic systems adding value in your work and organization?

:::


---
title: Deployment Patterns Across Organizational Layers
---

::grid{columns=5 width=100}

<v-click at=1>

:::box{height=35 span=2 align=top justify=left color=grey}
**Individual Augmentation**

- Personal assistants, task automation, decision support
- User-scoped permissions, personal context mgmt.
- E.g., scheduling, email triage, coding
  
:::

</v-click>

<v-click at=2>

:::box{span=3 align=top justify=left}
**Process Automation**

- Agent handles sub-process end-to-end
- Integrates with existing systems, workflow integration, system-level permissions
- E.g., document processing, data extraction, reports
:::

</v-click>

<v-click at=3>

:::box{height=30 span=5 align=center justify=left color=dark-blue}
**Autonomous Operations**

- Agent handles ongoing processes with minimal intervention
- Robust error handling, escalation protocols, comprehensive logging
- E.g., customer support, system monitoring, incident response

:::

</v-click>

::

<br>

<v-click at=4>

::grid{columns=1 width=100}

:::box{align=left justify=center text=md color=white}
➡️ Start with __augmentation__ (human in control), move to __automation__ (human
in the loop), and finally __autonomous__ operations (human on the loop).
:::
::

</v-click>


---
title: Agent Computer Interfaces
---

::box{align=center justify=center text=md color=white }
```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT DECISION LAYER                     │
│              (Reasoning, Planning, Tool Selection)          │
└─────────────────────────────────────────────────────────────┘
│
┌───────────────────┼───────────────────┐
│                   │                   │
▼                   ▼                   ▼
┌───────────────┐   ┌──────────────┐   ┌──────────────┐
│   UI-BASED    │   │  STRUCTURED  │   │   HYBRID     │
│  PERCEPTION   │   │     APIs     │   │  APPROACHES  │
└───────────────┘   └──────────────┘   └──────────────┘
```
::


---
title: Example - Car Configuration via Web Interface 
---
::prompt{tool=search w=[80%]}
    Please go to the BMW Configurator and configure me a BMW 3 Series sedan in black with more than 200 horse powers.
::

<br>
<br>
<br>

<v-click>

::grid{cols=1 width=80}
:::box{align=center justify=center height=10 width=70 color=dark-blue}
Let's have a look. 📺
:::
::

</v-click>

<br>
<br>

<v-click>

::grid{cols=1 width=80}
:::box{align=center color=white height=20}
▶️ The agent uses a hybrid approach to interact with the web
interface of the BMW Configurator. 

▶️ The query took __~11 minutes__ to complete.
:::
::

</v-click>


---
title: What are Agents?
align: center
---

::grid{cols=2 gap=md}

<v-click hide>

:::field{span=1}
::::imgx{src=./sections/shared_images/illustration_agent.png}
An agent according to it's definition. Illustration by Maarten Grootendorst.
::::
:::

</v-click>


<v-after>

:::field{span=1}
::::imgx{src=./sections/shared_images/illustration_agent_details.png}
Illustration by Maarten Grootendorst.
::::
:::

</v-after>

::

<!-- - **Environment** -- the world the agent interacts with
- **Tools** -- used to observe the environment
- **Memory** -- used to keep track of past inputs
- **Planning** -- reasoning about how to achieve goals
- **LLM(s)** -- “brain” or rules deciding how to go from observations to actions -->


---
title: Agents vs. Workflows
---

::grid{columns=2 width=100}
:::box{color=grey}
**🔄 Workflows**

LLMs and tools orchestrated through **predefined code paths**
:::

:::box{color=dark-blue}
**🤖 Agents**

LLMs **dynamically direct** their own processes and tool usage, maintaining control over task accomplishment
:::
::

<br>

<v-click>

*Note: Different definitions of "agents" -- from fully autonomous to prescriptive implementations.*

</v-click>


---
layout: Section
---

<div class="absolute top-50% left-5%">
  <div style="text-align: left; font-size: 3rem;">
    Building Blocks & Workflows
  </div>
  <div style="text-align: left; font-size: 1.2rem; margin-top: 2rem;">
    From foundational components to complex patterns
  </div>
</div>

---
title: The Augmented LLM
subtitle: Agentic Building Blocks
align: center
---

::grid{columns=1 gap=md width=90}
:::field{span=1}
::::imgx{src=./sections/shared_images/the_augmented_llm.png}
An LLM augmented by tools, memory, and retrieval. Illustration by Anthropic.
::::
:::
::

---
title: Prompt Chaining Workflow
subtitle: Agentic Building Blocks
---

**Decomposition into sequential steps -- each LLM call processes previous output**

<br>

::grid{cols=5 width=100}

:::field{span=3}
::::imgx{src=./sections/shared_images/prompt_chain_workflow.png width=80}
Prompt chaining workflow. Illustration by Anthropic.
::::
:::

:::box{color=white span=2}
**When to use:** Task easily decomposed into fixed subtasks. Trade latency for
higher accuracy.

<br>

**Examples:**
- Generate marketing copy → translate to different language
- Write outline → check criteria → write full document
:::
::

---
title: Routing Workflow
subtitle: Agentic Building Blocks
---

**Classify input and direct to specialized followup task**

<br>

::grid{cols=5 width=100}

:::field{span=3}
::::imgx{src=./sections/shared_images/routing_workflow.png width=80}
Routing workflow. Illustration by Anthropic.
::::

<br>

<v-click>

::::box{color=dark-blue span=3}
⁉️ How would you choose the models to use?
::::

</v-click>

:::

:::box{color=white span=2}
**When to use:** Complex tasks with distinct categories better handled separately, accurate classification possible

<br>

**Examples:**
- Direct customer queries to different processes (general, refunds, tech support)
- Route easy questions to Haiku, hard questions to Sonnet (cost/speed optimization)
:::
::

---
title: Parallelization Workflow 
subtitle: Agentic Building Blocks
---

**LLMs work simultaneously, outputs aggregated programmatically**

<br>

::grid{cols=5 width=100}

:::field{span=3}
::::imgx{src=./sections/shared_images/parallelization_workflow.png width=80}
Routing workflow. Illustration by Anthropic.
::::
:::

:::box{color=white span=2}
**When to use:** Subtasks can be parallelized for speed OR multiple perspectives
needed for confidence

**Sectioning:** Break into independent parallel subtasks

**Voting:** Run same task multiple times for diverse outputs
:::
::

---
title: Parallelization Workflow
subtitle: Agentic Building Blocks
---

::grid{columns=1 gap=md width=90}
:::box{color=dark-blue}
**Sectioning Examples:**
- **Guardrails:** One instance processes queries, another screens for inappropriate content
- **Automated evals:** Each LLM call evaluates different aspect of performance
:::

:::box{color=grey}
**Voting Examples:**
- **Code review:** Multiple prompts review and flag vulnerabilities
- **Content moderation:** Multiple prompts evaluate different aspects, different vote thresholds balance false positives/negatives
:::
::

---
title: Orchestrator Workflow
subtitle: Agentic Building Blocks
---

**Central LLM dynamically breaks down tasks, delegates to workers, synthesizes results**

<br>

::grid{cols=5 width=100}

:::field{span=3}
::::imgx{src=./sections/shared_images/orchestrator_workflow.png width=80}
Orchestrator workflow. Illustration by Anthropic.
::::
:::

:::box{color=white span=2}

**When to use:** Complex tasks where subtasks can't be predicted. Difference from parallelization: **flexibility** - subtasks determined by orchestrator based on input

<br>

**Examples:**
- Coding: Complex changes to multiple files (unpredictable scope)
- Search: Gathering and analyzing from multiple sources

:::
::

---
title: Evaluator-Optimizer Workflow
subtitle: Agentic Building Blocks
---

**One LLM generates response, another provides evaluation and feedback in a loop**


<br>

::grid{cols=5 width=100}

:::field{span=3}
::::imgx{src=./sections/shared_images/evaluator_optimizer_workflow.png width=80}
Evaluator-optimizer workflow. Illustration by Anthropic.
::::

<br>

<v-click>

::::box{color=dark-blue span=3}
⁉️ Where could this architecture be beneficial?
::::

</v-click>

:::

:::box{color=white span=2}

**When to use:** Improvement via clear evaluation criteria + iterative refinement. Signs: (1) Human feedback demonstrably improves responses, (2) LLM can provide such feedback

**Examples:**
- Translation with nuanced critiques
- Complex search requiring multiple rounds, evaluator decides if more needed
:::
::

---
layout: Section
---

<div class="absolute top-50% left-5%">
  <div style="text-align: left; font-size: 3rem;">
    Agents
  </div>
  <div style="text-align: left; font-size: 1.2rem; margin-top: 2rem;">
    Dynamic systems for open-ended problems
  </div>
</div>

---
title: Agents
subtitle: Overview
---

**Emerging as LLMs mature:** understanding complex inputs, reasoning/planning, tool use, error recovery

<br> 

::grid{columns=1 gap=sm width=90}
:::box{color=blue text=sm}
**Start:** Command from or interactive discussion with human
:::

:::box{color=dark-blue text=sm}
**Execution:** Plan and operate independently
:::

:::box{color=white text=sm}
**Feedback:** Gain "ground truth" from environment (tool results, code execution)
:::

:::box{color=grey text=sm}
**Checkpoints:** Return to human for information/judgement when needed
:::

:::box{color=white text=sm}
**Termination:** Upon completion or stopping conditions (max iterations)
:::
::

---
title: Reasoning and Acting Agent Architecture 
subtitle: Agentic Building Blocks
---

**LLMs using tools based on environmental feedback in a loop**

<br>

::grid{cols=5 width=100}

:::field{span=3}
::::imgx{src=./sections/shared_images/react_agent.png width=80}
Reasoning and Acting agent. Illustration by Anthropic.
::::
:::

:::box{color=white span=2}
**⚠️ Critical:**

- Design tool sets and documentation clearly and thoughtfully
- Provide relevant context and examples in prompts
- Implement robust error handling and fallback mechanisms
- Monitor and evaluate performance continuously

:::
::


---
title: Example - Customer Support
---

**Chatbot interfaces enhanced with tool integration**

::grid{columns=1 gap=sm width=90}
:::box{color=blue}
**✓** Natural conversation flow + access to external info/actions
:::

:::box{color=blue}
**✓** Tools for customer data, order history, knowledge base
:::

:::box{color=blue}
**✓** Programmatic actions (refunds, ticket updates)
:::

:::box{color=blue}
**✓** Clear success measurement (user-defined resolutions)
:::
::

<br>

:::box{color=white width=90}
**Viability:** Companies using usage-based pricing (charge only for successful resolutions)
:::


---
title: Summary
align: center
---

::grid{columns=1 gap=md width=80}
:::box{color=blue}
**Success ≠ Most Sophisticated System**

Success = Right System for Your Needs
:::
::

<br>

::grid{columns=1 gap=sm width=80}

:::box{color=white}
**1.** Start with simple prompts
:::

:::box{color=white}
**2.** Optimize with comprehensive evaluation
:::

:::box{color=white}
**3.** Add multi-step agentic systems only when simpler solutions fall short
:::

::
