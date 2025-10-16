---
layout: Section
---

<div class="absolute top-50%">
  <div style="text-align: left; font-size: 3rem;">
    Providing Toolboxes for Agents 🧰
  </div>
</div>


---
title: Tool Engineering
subtitle: Critical Component
---

::grid{columns=1 gap=md width=90}
:::box{color=grey text=lg}
**Tools are central to most agentic systems**

They deserve as much attention as your prompts
:::

:::box{color=blue text=md}
**How Tools Work:**

Enable Claude to interact with external services/APIs through specified structure and definition

Claude includes tool use block in API response when planning to invoke a tool
:::
::

---
title: Tool Format Considerations
subtitle: Format Matters for LLMs
---

::grid{columns=1 gap=md width=90}
:::box{color=dark-blue text=sm}
**Example:** Specifying file edits
- Write a diff (requires knowing line counts in advance)
- Rewrite entire file
:::

:::box{color=blue text=sm}
**Example:** Structured output
- Code in markdown (natural)
- Code in JSON (requires escaping newlines/quotes)
:::
::

:vspace{size=sm}

*Some formats are much harder for LLMs to write, despite being functionally equivalent*

---
title: Tool Format
subtitle: Key Suggestions
---

::grid{columns=1 gap=lg width=90}
:::box{color=white text=md}
**1. Give the model thinking space**

Enough tokens to "think" before writing itself into a corner
:::

:::box{color=blue text=md}
**2. Keep format natural**

Close to what model has seen on the internet
:::

:::box{color=dark-blue text=md}
**3. Minimize formatting overhead**

No accurate counting of thousands of lines, no string-escaping code
:::
::

---
title: Agent-Computer Interface (ACI)
subtitle: Design Principles
align: center
---

::grid{columns=1 width=80}
:::box{color=grey text=lg}
**💡 Rule of Thumb:**

Invest as much effort in ACI as you would in HCI (Human-Computer Interface)
:::
::

:vspace{size=lg}


---
title: Tool Documentation
subtitle: Best Practices
---

::grid{columns=1 gap=sm width=90}
:::box{color=blue text=sm}
**🤔 Put yourself in the model's shoes**

Is it obvious how to use this tool from description and parameters?
:::

:::box{color=white text=sm}
**📝 Write like for a junior developer**

Clear parameter names, comprehensive descriptions
:::

:::box{color=dark-blue text=sm}
**📚 Include essential details**

Example usage, edge cases, input format requirements, boundaries from other tools
:::

:::box{color=grey text=sm}
**⚠️ Especially important with similar tools**

Make distinctions clear
:::
::

---
title: Tool Testing & Iteration
---

::grid{columns=1 gap=lg width=90}
:::box{color=blue text=md}
**🧪 Test extensively**

Run many example inputs in workbench, see what mistakes the model makes
:::

:::box{color=white text=md}
**🔄 Iterate based on findings**

Adjust based on observed errors
:::

:::box{color=dark-blue text=md}
**🛡️ Poka-yoke your tools**

Change arguments to make mistakes harder (error-proofing)
:::
::

---
title: Real Example
subtitle: SWE-bench Tool Optimization
---

::grid{columns=1 gap=md width=90}
:::box{color=blue text=sm}
**Context:** Building agent for SWE-bench

*More time spent optimizing tools than overall prompt*
:::

:::box{color=grey text=sm}
**❌ Problem:**

Model made mistakes with relative filepaths after moving out of root directory
:::

:::box{color=white text=sm}
**✓ Solution:**

Changed tool to always require absolute filepaths
:::

:::box{color=blue text=sm}
**🎯 Result:**

Model used this method flawlessly
:::
::


---
title: Extending the ReAct Agent with More Tools ⌨️
text: lg
align: center
---

1. Open the file `src/tools/TASK.md` and read the description of the **second** (2️⃣) task.
2. Implement more tools for the MCP server by adding them in `src/tools/finance_tools/yahoo_finance.py` as needed. Feel free to
   implemented the suggested tools or create your own.


---
title: What have you built? What have you learned?
text: lg
align: center
---

Feel free to share your agents! 🚀 <v-click> ... and then we can grab a **coffee**! ☕️ </v-click>