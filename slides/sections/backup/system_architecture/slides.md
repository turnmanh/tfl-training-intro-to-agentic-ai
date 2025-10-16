---
layout: Section
---

<div class="absolute top-50%">

  <div style="text-align: left; font-size: 3rem;">
    System Interfaces
  </div>

</div>


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
::prompt{tool=search w=[70%]}
    Please go to the BMW Configurator and configure me a BMW 3 Series sedan in black with more than 200 horse powers.
::

<br>

<v-click>

::box{align=center color=white height=20}
▶️ The agent uses a hybrid approach to interact with the web
interface of the BMW Configurator. 

▶️ The query took __~11 minutes__ to complete.
::

</v-click>


---
title: Some Examples for Standardized Tooling
---

::grid{columns=3 width=100 gap=md}

<v-click>

:::field{align=end span=1}
::::imgx{src=./src/shared_images/logo_atlassian.png}
MCP-Atlassian
::::
:::

</v-click>
<v-click>

:::field{align=end span=1}
::::imgx{src=./src/shared_images/logo_playwright.svg}
Playwright MCP
::::
:::

</v-click>
<v-click>

:::field{align=end span=1}
::::imgx{src=./src/shared_images/logo_mcp_registry.png}
MCP Registry
::::
:::

</v-click>

::