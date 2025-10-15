---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Orchestration & Governance
  </div>
</div>

---
title: The Control Paradox
---

::grid{columns=2 width=100}

:::box{span=1 align=top justify=left}
**Targeted scenario:**

- Agent handles complete processes
- Ability to adapt dynamically  
- Autonomy to access tools, data, transactional systems, ...

:::

:::box{span=1 align=top justify=left}
**Required control:**

- Approval for certain actions
- Action scopes and tool registries 
- Authentication 
- Traceability of actions
:::

::

<br>

::box{color=white text=md}
**Question:** How do we orchestrate agent behavior for autonomy *and* control?
::


---
title: Orchestration Architecture & Core Orchestration Components
---

Orchestration is the _control layer_ that defines __capabilities, boundaries,
and interactions__ of agents within an ecosystem. It supports the __coordination
of multiple agents__ while providing __observability & reusability__.

<br>

::grid{columns=4 width=100 gap=md}

<v-click>

:::box{align=top justify=left text=md color=white}
**Agent Runtime**
- Secure execution environment
- Resource & lifecycle management
- Evaluation & observability
:::

</v-click>
<v-click>

:::box{align=top justify=left text=md color=grey}
**State Management**
- Memory management
- Checkpointing & context tracking
:::

</v-click>
<v-click>

:::box{align=top justify=left text=md color=blue}
**Tool Registry**
- Central catalog
- Permissions
- Monitoring
:::

</v-click>
<v-click>

:::box{align=top justify=left text=md color=dark-blue}
**Coordination Protocols**
- Agent communication
- Delegation
- Conflict resolution
:::

</v-click>

::

<br>

<v-click>

::box{color=white} 
Orchestration platforms can be chosen according to the **industry's
requirements**: _Fully-visible graph-based_ for regulated industries;
_event-driven or role-based_ for efficiency in less regulated contexts. 
::

</v-click>


---
title: Advantages of Orchestration Platforms within Organizations
---

::grid{columns=3 width=100 gap=md}

:::box{height=35 span=1 align=top justify=left text=md color=grey}
**Self-service**

 -  Adapt workflows without engineering
 -  Empower business users
 -  Built-in evaluation 
:::

:::box{height=35 span=1 align=top justify=left text=md color=grey}
**Integrability**

 -  Connectors to common systems
 -  API-first design
 -  Extensible tool registry
:::

:::box{height=35 span=1 align=top justify=left text=md color=grey}
**Scalability**

 -  Reusable connectors
 -  Standardized integrations
 -  Centralized governance
:::

::

<br>
<br>

<v-click>

::box{height=10 align=center justify=center color=white}

➡️ n8n, dify.ai, LangGraph, MS Agent Framework, CrewAI, OpenAI's AgentKit, Google's Opal, ...

::

</v-click>
