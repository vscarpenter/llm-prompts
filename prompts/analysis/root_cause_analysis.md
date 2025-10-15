# Root Cause Analysis

## Prompt
> Conduct a root cause analysis to identify the underlying cause of this problem.
>
> Problem statement: "{{problem_description}}"
> Symptoms observed: "{{what_went_wrong}}"
> When it occurred: "{{timeline}}"
> Impact: "{{consequences}}"
> Context: "{{background_information}}"
>
> **Root Cause Analysis:**
>
> **1. Problem Definition**
> - Clear problem statement
> - Quantified impact (cost, time, affected users, etc.)
> - Why this problem matters
>
> **2. Timeline of Events**
> - What happened first
> - Sequence of events leading to problem
> - When problem was detected
>
> **3. Five Whys Analysis**
>
> **Problem**: [State the problem]
>
> **Why #1**: Why did this happen?
> → [Answer]
>
> **Why #2**: Why did [answer from Why #1] happen?
> → [Answer]
>
> **Why #3**: Why did [answer from Why #2] happen?
> → [Answer]
>
> **Why #4**: Why did [answer from Why #3] happen?
> → [Answer]
>
> **Why #5**: Why did [answer from Why #4] happen?
> → [Root cause identified]
>
> **4. Fishbone Diagram (Ishikawa)**
>
> **Problem**: [Problem statement]
>
> **Categories of causes:**
>
> **People:**
> - Contributing factor 1
> - Contributing factor 2
>
> **Process:**
> - Contributing factor 1
> - Contributing factor 2
>
> **Technology/Tools:**
> - Contributing factor 1
> - Contributing factor 2
>
> **Environment:**
> - Contributing factor 1
> - Contributing factor 2
>
> **Management:**
> - Contributing factor 1
> - Contributing factor 2
>
> **5. Root Cause(s) Identified**
> - Primary root cause: [What fundamentally caused this]
> - Contributing factors: [Other causes that enabled it]
> - Systemic issues: [Patterns or gaps that allowed this]
>
> **6. Evidence & Validation**
> - How we know this is the root cause
> - Data or observations that support this
> - Tests to confirm
>
> **7. Corrective Actions**
>
> **Immediate fixes** (stop the bleeding):
> - [ ] Action 1 (Owner, Due date)
> - [ ] Action 2 (Owner, Due date)
>
> **Long-term solutions** (prevent recurrence):
> - [ ] Action 1 (Owner, Due date)
> - [ ] Action 2 (Owner, Due date)
>
> **Preventive measures** (catch similar issues earlier):
> - [ ] Action 1 (Owner, Due date)
> - [ ] Action 2 (Owner, Due date)
>
> **8. Success Metrics**
> - How we'll measure if corrective actions worked
> - Leading indicators to monitor
> - Review date to assess effectiveness

## Tips / Notes
- Specify method: "use 5 Whys," "use Fishbone diagram," "use Fault Tree Analysis"
- Add context: "production incident," "process failure," "quality issue"
- Request depth: "quick RCA" or "comprehensive investigation"
- For teams: "blameless RCA format" (focus on systems, not individuals)

## Variants
- "Incident post-mortem" (blameless, timeline-focused)
- "Process failure analysis" (workflow and handoff issues)
- "Quality issue RCA" (defect or bug analysis)
- "Safety incident analysis" (critical failure with preventive focus)
