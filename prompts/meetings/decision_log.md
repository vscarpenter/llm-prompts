---
domain: meetings
version: 1.1
author: llm-prompts
---

# Decision Log

## Prompt
> You are documenting an important decision made during a meeting or discussion.
>
> Decision: "{{decision_made}}"
>
> **Date:** "{{YYYY-MM-DD}}"
> **Deciders:** "{{people}}"
> **Status:** "{{Proposed|Decided|Implemented}}"
>
> ## Context
> What situation led to needing this decision? What were we trying to solve?
>
> ## The Decision
> What did we decide to do? Be specific and clear.
>
> ## Rationale
> Why did we make this choice?
> - Key reasons and considerations
> - What factors were most important
>
> ## Options Considered
> 1. "{{Option}}" - Why we chose this or didn't choose it
> 2. "{{Option}}" - Pros and cons
>
> ## Implications
> - What changes as a result of this decision?
> - Who is affected?
> - What needs to happen next?
>
> ## Follow-up Actions
> - [ ] {{Action}} - Owner: {{name}}
> - [ ] {{Action}} - Due: {{date}}
>
> ## Related Decisions/References
> - Links to related discussions, docs, or previous decisions
>
> Keep it factual and concise. This should help someone understand why this decision was made.

## Output Format
+- A concise decision log with date, deciders, status, rationale, and next steps.

## Variants
+- "Quick Decision Record" - minimal fields
+- "Product Decision Log" - include customer impact, metrics
