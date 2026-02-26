---
layout: Section
---

🤖 Introduction to Agentic Systems


---
title: From GenAI Adoption to Agentic AI Impact
align: center
---

:::box{mt=-15 color=grey justify=center}
**_"Nearly eight in ten companies report using gen AI—yet just as many report no
significant bottom-line impact."_**,  
—McKinsey, March 2025
:::


---
title: From GenAI Adoption to Agentic AI Impact
---

:::box{color=grey justify=center}
**_"Nearly eight in ten companies report using gen AI—yet just as many report no
significant bottom-line impact."_**,  
—McKinsey, March 2025
:::


::grid{columns=2 mt=8}
:::field{}
* **Adoption is no longer the question**
    * GenAI experimentation is widespread
    * Tools are embedded in workflows across functions. 
* **Creating impact is the real challenge**
    * Limited measurable cost reduction or revenue growth
    * Productivity gains remain local and incremental
    * AI is assisting work, not doing the work
:::

:::field{}
* **Agency is the missing link**  
  To move from experimentation to economic value, AI must:
    * Operate at the core of the organization
    * Execute actions towards the business goals
    * Make decisions within defined boundaries
:::
::



---
title: The Transition from "AI that Helps" to "AI that Does"
align: center
---

::grid{columns=2 width=100}
:::box{color=grey}
Previously: **AI that helps**
- Improved tooling
- Autocomplete for emails
- Suggestions in your IDE
- Insights from your data
- "Would you like me to draft that?"
:::

:::box{color=dark-blue}
Now: **AI that does**
- Agents that complete multi-step workflows
- Systems make decisions within defined parameters
- AI maintains context within set scopes
- Software coordinates with other software
:::
::

:img{src=./img/large-arrow.drawio.svg w=120 mx=auto mt=5}



---
title: "Example: Car Configuration via Web Interface"
align: center
---
::prompt{tool=agent w=[75%] mt=-10}
    Please go to the BMW Configurator and configure me a BMW 3 Series sedan in black with more than 200 horse powers.
::


---
title: Process Characteristics Suitable for Agent Employment
align: center
---

::grid{columns=4 width=100 gap=md}
:::box{color=white}
**High Coordination Effort**

 - Multiples systems
 - Context switching
 - Manual data aggregation

:::

:::box{color=grey}
**Ambiguity**

 - Judgment on incomplete data
 - Unstructured inputs
 - Exceptions that don't fit rigid rules

:::

:::box{color=blue}
**Dynamic Environment**

 - Intermediate results determine path
 - Iterative refinement 

:::

:::box{color=dark-blue}
**Knowledge-intensive Operations**

 - Requires synthesis of information
 - Domain expertise at scale

:::

<v-click>

:::field{justify=center span=4 mt=5}
**❌ Where they don't fit:** High-volume tasks, deterministic paths,
safety-critical operations, ...
:::

</v-click>
::







---
layout: Section
---

🤖 Agentic Systems: Building Blocks


---
title: Standard LLM Call
subtitle: Baseline model
align: center
---

::grid{columns=2 width=100}

:::field{}
**Pattern:**  
Prompt → Model → Response

**Characteristics:**

* Single request-response interaction
* All context must fit in the prompt
* Model cannot verify or act on external systems
:::

:::field{justify=center}
:img{src=./img/standard-llm-call.drawio.svg h=40}
:::
::



---
title: Augmented LLM
subtitle: Capability-enhanced model
align: center
---

::grid{columns=2 width=100}

:::field{}
**Pattern:**  
Prompt → Model ←→ Tools → Response

**New capabilities:**

* **Tool calling** (APIs, search, code execution, databases)
* **Memory** (conversation history, long-term state)
* Optional short internal tools loops before final answer
:::

:::field{align=center}
:img{src=./img/augmented-llm.drawio.svg h=45}
:::

::

:vspace{size=lg}

::span{text=xs}
**Source:** https://www.anthropic.com/engineering/building-effective-agents
::



---
title: LLM Orchestration Patterns
subtitle: Control flows
align: center
---

LLM capabilities can be orchestrated in different ways, with the appropriate pattern determined by your use case, the level of autonomy required, and your reliability constraints.

:vspace{size=lg}

::grid{columns=3 width=100 pb=5}
:::box{color=white}
**LLM feature**

A single LLM-powered capability embedded in a product, typically implemented as
one model call (prompt → output)
:::

:::box{color=blue}
**LLM workflow**

A multi-step system where LLM calls and tools are orchestrated through
predefined code paths (fixed control flow)
:::

:::box{color=dark-blue}
**Agent**

A system where the LLM dynamically decides what to do next, typically running
tools in a loop until a stop condition is met.
:::
::


---
layout: Section
---

💪 LLM Features


---
title: LLM Feature
subtitle: Model-powered capability embedded inside an application
layout: twocols
---

::left::

* The **application calls an LLM** to generate, transform,, or evaluate content in
  response to a user request.
* May be implemented as an augmented LLM call
* The application controls the inputs, constraints, and outputs

:vspace{size=md}

:img{src=./img/llm-feature.drawio.svg w=90 mt=8 mx=auto}


::right::

**Example:** Text refinement and writing assistance

:img{src=./img/llm-feature-google-docs.png w=120 class="border-solid border-1" shadow=lg mx=auto mt=5}


---
layout: Section
---

💪💪 LLM Workflows


---
title: LLM Workflow
subtitle: Prompt chaining
---

Prompt chaining means breaking tasks into **multiple sequential LLM calls, where
the output of one step becomes the input of the next step**. The order of the
steps is predefined in code.


:img{src=./img/llm-prompt-chaining.drawio.svg w=150 mx=auto my=9}



**Example:** Email processing pipeline (*receive email* → *classify* → *label* → *draft reply* → *notify user*)

::::div{text=xs mt=5}
**Source:** https://www.anthropic.com/engineering/building-effective-agents
::::



---
title: Advanced LLM Workflows
subtitle: Router workflow
align: center
---

The **LLM Router workflow** is used when a single prompt or model is not the most
effective way to handle a task. Instead, first classify (i.e., route) the input,
then send it to a specialized follow-up task.

::grid{columns=2 mt=5}
:::field{text=sm}
**When to use:**

* **Heterogeneous task types:** each task performs better with a different system
  prompts and/or model.
* **Cost optimizations:** route simple queries to cheaper/faster models and complex
  ones to more capable models.
* **Different output formats:** JSON, Markdown, plain text, etc.
* **Safety segmentation:**  route high-risk inputs to more constrained prompts
  or include human review.
:::

:::field{mt=8}
:img{src=./img/routing_workflow.png w=100 mx=auto rounded=lg shadow=lg}

::::div{text=xs mx=auto mt=5}
*Illustration by Anthropic.*
::::
:::
::



---
title: Advanced LLM Workflows
subtitle: Parallelization workflow
align: center
---

The **Parallelization workflow** runs multiple LLM calls
independently and aggregates their results afterwards.

::grid{columns=2 mt=5}
:::field{text=sm}
**When to use:**

* **Independent subtasks:** when a larger task can be broken in subtask that do
  not depend on each other, running them in parallel reduces wall-clock time.
* **Ensemble/multi-perspective reasoning:** improve reliability and robustness
  via ranking, voting, and merging.
* **Independent evaluations:** get multiple perspectives on the same input.
* **Map-reduce problems:** process chucks independently, then combine the
  results.
:::

:::field{mt=8}
:img{src=./img/parallelization_workflow.png w=100 mx=auto rounded=lg shadow=lg}

::::div{text=xs mx=auto mt=5}
*Illustration by Anthropic.*
::::
:::
::


---
title: Advanced LLM Workflows
subtitle: Orchestrator workflow
align: center
---

The **Orchestrator workflow** is used when a task requires planning, coordination,
and adaptive control across multiple steps. This includes **complex, multi-step
problems** where a solution cannot be predefined as a fixed pipeline.

::grid{columns=5 mt=5}
:::field{span=2 text=sm}
The **orchestrator**:

* Breaks a task into steps
* Decides the execution order
* Calls the sub-tasks (LLM calls, agents, etc.)

:vspace{size=sm}

The **synthesizer** combines the results to form the output.

:::

:::field{span=3 mt=1}
:img{src=./img/orchestrator_workflow.png w=100 mx=auto rounded=lg shadow=lg}

::::div{text=xs mx=auto mt=5}
*Illustration by Anthropic.*
::::
:::
::



---
title: Advanced LLM Workflows
subtitle: Evaluator-optimizer workflow
align: center
---

The **Evaluator-Optimizer Workflow** iteratively improves the output quality
through structured feedback. 

The **Optimizer** produces or revises output, the
**Evaluator** critiques or scores it. The loop repeats until quality criteria
are met.

::grid{columns=2 mt=5}
:::field{text=sm}
**When to use:**

* **Meeting quality thresholds:** the evaluator checks whether the output meets
  the defined criteria before approval.
* **Iterative refinement:** instead of hoping for a perfect first draft, the
  system refines progressively.
* **Costly failure:** when low-quality outputs are unacceptable, doing multiple
  passes reduces risk.
:::

:::field{mt=2}
:img{src=./img/evaluator_optimizer_workflow.png w=100 mx=auto rounded=lg shadow=lg}

::::div{text=xs mx=auto mt=4}
*Illustration by Anthropic.*
::::
:::
::


---
layout: Section
---

💪💪💪 AI Agents


---
title: Agents Overview
subtitle: "Emerging as LLMs mature: understanding complex inputs, reasoning, tool use"
---

::grid{columns=1 gap=sm width=60}
:::box{color=grey text=sm}
**Start:**  
Command from or interactive discussion with human
:::

:::box{color=dark-blue text=sm}
**Execution:**  
Plan and operate independently
:::

:::box{color=white text=sm}
**Feedback:**  
Gain "ground truth" from environment
:::

:::box{color=blue text=sm}
**Checkpoints:**  
Return to human for information/judgement when needed
:::

:::box{color=white text=sm}
**Termination:**  
Upon completion or stopping conditions
:::
::

---
title: AI Agent
subtitle: Reasoning and acting agent architecture
align: center
---

An AI agent is a goal-directed system in which the **LLM itself decides which
steps to take** to achieve a specified objective.

:vspace{size=md}

::grid{columns=2}
:::field{}
Typical execution cycle:

1. **Thought:** Analyze the current state and decide on the next step
2. **Action:** Interact with the environment via tool calls.
3. **Observation:** Observe the environment by inspecting tool outputs.
4. Incorporate new information. Repeat.
:::

:::field{}
:img{src=./img/react-architecture.drawio.svg w=90 mx=auto mt=4}

::::div{text=sm mx=auto mt=8}
*ReAct agent architecture.*
::::
:::

---
title: AI Agent
subtitle: Reasoning and acting agent architecture
---

An AI agent is a goal-directed system in which the **LLM itself decides which
steps to take** to achieve a specified objective.

:vspace{size=md}

::grid{columns=2}
:::field{}
1. **Goal & instructions** (system prompt, constraints)
2. **Model** (LLM capable of tool calling and structured outputs)
3. **Tools** (APIs, search, code execution)
4. **Memory** (short-term, long-term)
5. **Execution harness**
    * Executes tool calls, enforces iteration limits and stop conditions
6. **Guardrails**
    * Validators, sandboxes, human-in-the-loop checkpoints, tracing
:::

:::field{}

:img{src=./img/agent-building-block.drawio.svg my=auto}
:::
::



---
title: Example AI Agent
subtitle: Drafting a LinkedIn post
align: center
---

::prompt{tool=search w=[80%]}
    Find the three most recent talks about agentic AI at PyData, summarize each in two sentences, and draft a short LinkedIn post about it.
::



---
title: Example AI Agent Conversation Trace
subtitle: Agent with tool calls
layout: twocols
---

::left::

**System message:**

```json
{
    "role": "system",
    "content": "You are an AI agent. Your task is to 
                achieve the user's  goal using the 
                available tools. You may call tools 
                when needed. Stop when the task is 
                finished.",
    "tools": ["web_search", "extract_text"]
}
```

::right::

**User message:**

```json
{
    "role": "user",
    "content": "Find the three most recent talks about 
                agentic AI at PyData, summarize each in
                two sentences, and draft a short 
                LinkedIn post about it."
}
```


---
title: Example AI Agent Conversation Trace
subtitle: Agent with tool calls
layout: twocols
---

::left::

**Assistant → Tool call `web_search`:**

```json
{
    "role": "assistant",
    "tool_call": {
        "name": "web_search",
        "arguments": {
            "query": "agentic ai talks pydata"
        }
    }
}
```

::right::

**Tool `web_search` result:**

```json
{
    "role": "tool",
    "name": "web_search",
    "content": [
        {"title": "...", "url": "...", "date": "..."},
        {"title": "...", "url": "...", "date": "..."},
        {"title": "...", "url": "...", "date": "..."}
    ]
}
```


---
title: Example AI Agent Conversation Trace
subtitle: Agent with tool calls
layout: twocols
---

::left::

**Assistant → Tool call `extract_text`:** (3x)

```json
{
    "role": "assistant",
    "tool_call": {
        "name": "extract_text",
        "arguments": {
            "url": "https://...",
            "format": "markdown"
        }
    }
}
```

::right::

**Tool `extract_text` result:** (3x)

```json
{
    "role": "tool",
    "name": "extract_text",
    "content": "# An introduction to Agentic AI
                ..."
}
```


---
title: Example AI Agent Conversation Trace
subtitle: Agent with tool calls
align: center
---

**Assistant → Final answer:**

```json
{
    "role": "assistant",
    "content": "Summary 2: ...\n\nSummary 2: ...\n\nSummary 3: ...\n\nLinkedIn post: ..."
}
```


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
