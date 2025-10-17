---
title: BACKUP - Different Governance Dimensions
layout: twocols
---

If agents operate autonomously, governance must ensure **safety**, **compliance**, and **reliability**.

::grid{columns=5 width=100 gap=md}
:::box{span=1 align=top justify=left}
**1. Access Control**
- Fine-grained permissions
- Least privilege
- Dynamic adjustment
- Audit logging
:::
:::box{span=1 align=top justify=left}
**2. Behavioral Guardrails**
- Input: topic/content filtering, injection detection
- Output: hallucination, PII, bias, filtering
- Action: approval, rate limits, rollback
:::
:::box{span=1 align=top justify=left}
**3. Monitoring & Observability**
- Traces, metrics, logs, evaluations
- Real-time dashboards
- Anomaly detection
- Distributed tracing
:::
:::box{span=1 align=top justify=left}
**4. Human-in-the-Loop (HITL)**
- Manual approval, confidence thresholds, periodic review
- HITL adds latency—design for autonomy within bounds
:::
:::box{span=1 align=top justify=left}
**5. Risk & Compliance**
- Risk tiers: high, moderate, minimal
- Regulatory frameworks: EU AI Act, GDPR, HIPAA
:::
::

<br>

**Emerging Pattern:** Governance agents monitor, detect, and remediate issues.

**Key Takeaway:** Governance is foundational for scaling. Build it from day one.


---
title: BACKUP - Orchestration Frameworks
align: center
---
::grid{columns=2 width=100}

:::box{span=1 align=top justify=left}
**Graph-Based (LangGraph):**
- State graphs, deterministic paths
- Time-travel debugging
- Best for: Transparency, auditability

**Event-Driven (MS Agent Framework):**
- Async events, loose coupling
- Dynamic agent discovery
- Best for: Distributed systems
:::
:::box{span=1 align=top justify=left}
**Role-Based (CrewAI):**
- Agents with roles, hierarchical coordination
- Team-like patterns
- Best for: Collaboration

**Platform-Managed (AWS, Google):**
- Managed runtime, monitoring, scaling
- Best for: Enterprises
:::
::

<br>

::box{color=white text=sm}
**Design Principle:**
Choose frameworks based on transparency needs. Regulated industries require graph-based architectures; others may use event-driven or role-based for efficiency.
::