# Architecture Decision Record (ADR)

## Prompt
> You are a software architect documenting an important technical decision.
>
> Create an Architecture Decision Record for: {{decision_description}}
>
> Follow this structure:
>
> # ADR {{number}}: {{Title of Decision}}
>
> **Status:** {{Proposed | Accepted | Deprecated | Superseded}}
> **Date:** {{YYYY-MM-DD}}
> **Deciders:** {{List of people involved}}
>
> ## Context
> What is the issue we're facing? What factors are influencing this decision? What are the constraints?
>
> ## Decision
> What are we doing? State the decision clearly and concisely.
>
> ## Consequences
>
> **Positive:**
> - What becomes easier or better
>
> **Negative:**
> - What becomes harder or worse
> - What tradeoffs are we accepting
>
> **Neutral:**
> - Other impacts to be aware of
>
> ## Alternatives Considered
> What other options did we evaluate? Why were they rejected?
>
> ## References
> - Links to related discussions, RFCs, or documentation
>
> Be specific and factual. Focus on "why" over "how". An ADR should help future developers understand the reasoning, not just the outcome.

## Tips / Notes
- Use ADRs for significant decisions: framework choices, database selection, major architectural patterns
- Keep them immutable - if a decision changes, create a new ADR that supersedes the old one
- Store ADRs in version control (e.g., `docs/adr/` directory)
- Number them sequentially (001, 002, etc.)

## Example Usage
Replace `{{decision_description}}` with:
- "Using PostgreSQL instead of MongoDB for our primary database"
- "Adopting microservices architecture"
- "Choosing React over Vue for frontend framework"
