# Notes on Agents

We provided the two agent architectures as Mermaid flowcharts in `./charts/`.

## Reasoning & Acting Agent

**Q:** What are the potential pitfalls of using a reasoning and acting agent on
longer tasks that require multiple steps?

**A:** The agent might generate too much output, leading to confusion or
irrelevant steps. It might lead loss of focus on the main task.

## Plan & Execute Agent

**Q:** What errors might occur if the agent's plan is not well-structured or if
the planning is not constrained?

**A:** Too many output tokens, irrelevant steps, or overly detailed instructions
that are not actionable.

**Q:** What are potential considerations when targeting efficient execution in a
plan and execute agent?

**A:** The agent should focus on high-level steps, avoid unnecessary details.
Running a re-planner every step increases LLM calls dramatically. Finally, one
could think about a more efficient / smaller model. Generally, different models
could be used for different steps.
