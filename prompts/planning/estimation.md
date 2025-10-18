---
domain: planning
version: 1.1
author: llm-prompts
---

# Task Estimation

## Prompt
> You are an engineering lead helping estimate work complexity and timeline.
>
> Task to estimate: "{{task_description}}"
>
> Provide an estimation breakdown:
>
> ## Task Summary
> Restate what needs to be built in 1-2 sentences
>
> ## Complexity Assessment
>
> **Known Complexity:**
>- Parts we understand well
>- Existing patterns we can follow
>
> **Unknown Complexity:**
>- Parts requiring research or investigation
>- New patterns or technologies
>- External dependencies
>
> ## Work Breakdown
> 1. [Subtask] - Estimated time, confidence level (high/medium/low)
> 2. [Subtask] - Dependencies or blockers
> 3. [Testing] - Time for unit tests, integration tests
> 4. [Code Review & Iteration] - Review cycles, addressing feedback
>
> ## Time Estimate
> - Best case: {{X}} hours
> - Most likely: {{Y}} hours
> - Worst case: {{Z}} hours
> 
> **Recommendation:** Plan for {{Y}} hours, buffer for {{Z}}
>
> ## Risk Factors
> What could make this take longer?
> - Technical risks
> - Dependency on other teams
> - Unclear requirements
>
> ## Confidence Level
> {{High | Medium | Low}} - Explain why
>
> Be realistic, not optimistic. Account for testing, code review, and iteration time.

## Tips / Notes
- Use t-shirt sizes for rough estimates
- Include time for documentation and deployment
- If confidence is low, spike/investigate first before committing to timeline
- Multiply your initial estimate by 1.5-2x for more accuracy

## Variants
- Story Point Estimation - Convert to story points using Fibonacci scale with justification
- Team Velocity Planning - Estimate multiple tasks for sprint planning with capacity considerations
