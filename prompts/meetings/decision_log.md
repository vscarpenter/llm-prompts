# Decision Log

## Prompt
> You are documenting an important decision made during a meeting or discussion.
>
> Create a decision record for: {{decision_made}}
>
> Use this format:
>
> # Decision: {{Short Title}}
> **Date:** {{YYYY-MM-DD}}
> **Deciders:** {{People who made the decision}}
> **Status:** {{Proposed | Decided | Implemented}}
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
> 1. **{{Option}}** - Why we chose this or didn't choose it
> 2. **{{Option}}** - Pros and cons
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
> Keep it factual and concise. This should help someone understand why this decision was made 6 months from now.

## Tips / Notes
- Use for cross-team decisions, product direction, significant process changes
- Different from ADRs (which are specifically for architecture)
- Store in shared location (wiki, docs folder, project management tool)
- Review periodically to see if decision still makes sense

## Variants
**Quick Decision Record** - Simplified version with just Decision, Rationale, and Next Steps

**Product Decision Log** - Add customer impact, metrics to track, success criteria
