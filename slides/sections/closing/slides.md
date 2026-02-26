---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    It's a Wrap! 🎬
  </div>
</div>


---
title: When Is Agentic AI the Right Choice?
---

Agentic AI is most justified when the task is goal-directed, multi-step, and the
execution path is difficult to predefine in advance.

:vspace{size=md}

::grid{columns=2 width=100}
:::field{}

* **Open-ended execution**:
    * Unpredictable number of steps
    * Cannot be reliably implemented as fixed workflow
* **Essential tools use**:
    * Requires APIs, databases, code execution, etc.
    * Real-world interaction is part of the task
* **Feedback loops available**:
    * The system can validate progress using tools, tests, rules, and external
      state

:::
:::field{}

* **Clear success criteria**:
    * Objective definition of done
* **Safe execution environment**:
    * Sandbox or execution harness
    * Human checkpoints and oversight
* **Sufficient business value**:
    * Justify latency, costs, and engineering complexity

:::
::

---
title: "Levels of autonomy: augmentation, automation, and autonomous operations"
subtitle: Deployment patterns across organizational layers
align: center
justify: center
---

::grid{columns=3 width=100}
:::box{color=white}
**Individual augmentation**

* Personal assistants, task automation, decision support
* User-scoped permissions, personal context management
:::

:::box{color=blue}
**Process automation**

* Agent handles a (sub)process end-to-end
* Integration with existing systems and workflows
* System-level permissions
:::

:::box{color=dark-blue}
**Autonomous operations**

* Agent handles ongoing processes with minimal intervention
* Robust error handling, escalation protocols, logging
:::
::

:vspace{size=lg}

:img{src=./img/increasing-autonomy.drawio.svg w=200 mx=auto}

:vspace{size=md}

::div{text=sm}
**Note:** You do not aim for increasing autonomy. In practice, you pick the
lowest level that meets the use case.
::



---
title: "Levels of human involvement: in-the-loop, on-the-loop, over-the-loop"
subtitle: Deployment patterns across organizational layers
---

The level of human involvement and oversight depends on risk, reversibility, and
the required accountability for a use case:

:vspace{size=lg}

::grid{columns=3}
:::box{color=white}
**Human-in-the-loop**

Human approval is required before critical actions. AI produces suggestions,
human validates, edits, or rejects. Emphasis on oversight and accountability.
:::

:::box{color=blue}
**Human-on-the-loop**

AI executes autonomously within boundaries. Human monitors and can intervene.
Alerts and logging is in place. Focus on supervision.
:::

:::box{color=dark-blue}
**Human-out-the-loop**

AI acts autonomously end-to-end. No real-time human supervision. Relies on
validation, testing, and safeguards. Periodic human audits.
:::

:::field{justify=center text=sm}
**high-risk** and regulated environments
:::

:::field{justify=center text=sm}
**medium-risk** operational workflows
:::

::field{justify=center text=sm}
**low-risk** or reversible actions
::
::grid

---
title: Wrapping Up - Three Core Principles Building Agentic Systems 
---

::grid{columns=1 gap=lg width=90}
:::box{color=blue text=lg}
**1️⃣ Maintain Simplicity**

In your agent's design
:::

:::box{color=white text=lg}
**2️⃣ Prioritize Transparency**

Explicitly show agent's planning steps
:::

:::box{color=dark-blue text=lg}
**3️⃣ Craft Agent-Computer Interface (ACI)**

Through thorough tool documentation and testing
:::
::


---
title: Wrapping Up - The Shift to "AI that Does"
---

::box{color=white span=3 height=15}
▶️ With the rise of AI agents, the focus is shifting from "AI that thinks" to "AI
that does". 
::

<br>

::box{color=grey span=3 height=15}
▶️ In order to harness the full potential of AI agents, standardized and robust
interfaces are essential.
::

<br>

::box{color=blue span=3 height=15}
▶️ Orchestration platforms provide the necessary infrastructure to manage and
coordinate multiple AI agents.
::

<br>

::box{color=dark-blue span=3 height=15}
▶️ There's no such thing as free lunch!
::


---
title: Any last questions?
align: center
---

::grid{cols=1 width=70}

<v-click>

:::box{align=center text=lg color=blue}
Feel free to ask any last questions you might have! ... or approach us via
email.
:::

</v-click>

<br>
<br>

<v-click>

:::box{align=center text=lg color=dark-blue}
Thank you for participating in today's workshop! 

We hope you enjoyed it and found it valuable. 🚀

We'd love to hear your feedback! ➡️
🔗[Survey](https://forms.gle/XVuCbmyaqMnheRbi8)
:::

</v-click>

::

