---
domain: meetings
version: 1.1
author: llm-prompts
---

# Technical Discussion Facilitator

## Prompt
> You are structuring a focused technical discussion to reach a decision or alignment.
>
> Topic: {{technical_topic}}
> Goal: {{what_we_need_to_decide}}
>
> Create a discussion guide:
>
> # Technical Discussion: {{Topic}}
> **Date:** {{date}}
> **Attendees:** {{key people who should be involved}}
> **Duration:** {{estimated time}}
>
> ## Objective
> What we need to accomplish in this discussion (specific outcome)
>
> ## Background / Context
> Briefly: why are we having this discussion now? What's the current state?
>
> ## Key Questions to Answer
> 1. {{Question}} - What we need to decide or align on
> 2. {{Question}} - Critical consideration
> 3. {{Question}} - Success criteria or constraints
>
> ## Options to Discuss
>
> ### Option 1: {{Name}}
> - **How it works:** Brief description
> - **Pros:**
> - **Cons:**
> - **Effort:** Rough estimate
>
> ### Option 2: {{Name}}
> - **How it works:** Brief description
> - **Pros:**
> - **Cons:**
> - **Effort:** Rough estimate
>
> ## Evaluation Criteria
> How will we decide between options?
> - Performance requirements
> - Maintainability
> - Time to implement
> - Team expertise
>
> ## Decision Process
> - Everyone reviews options beforehand
> - Discuss unknowns and risks
> - Identify any need for prototyping
> - Make recommendation or decision
>
> ## Next Steps
> Based on decision:
> - [ ] {{Action if we choose Option 1}}
> - [ ] {{Action if we choose Option 2}}
>
> **Pre-work:** Share this doc 48 hours before meeting. Ask attendees to review and add questions.
+
+## Output Format
+- A structured discussion guide with objective, context, and decision path.
+
+## Variants
+- "Design Review" - Focus on feedback for a proposed solution
+- "Architecture Discussion" - Include system diagrams and scalability
+- "Technical Spike Review" - Present findings from investigation with recommendations
