---
domain: business
version: 1.1
author: llm-prompts
---

# Value Proposition

## Prompt
> Define a clear value proposition for a product or service.
>
> Product: "{{product}}"
> Customer job: "{{customer_job}}"
> Pain points: "{{pains}}"
> Gain creators: "{{gains}}"
> Differentiation: "{{how_different_from_competitors}}"
>
> **Output:** A concise value proposition statement and supporting bullets.

## Output Format
- Value proposition statement (one line).
- 2-4 supporting bullet points.

## Sample Output
```markdown
We help {{customer}} by solving {{pains}} with {{product}} so they can {{gains}}.
- Benefit 1: ...
- Benefit 2: ...
```

## Tips / Notes
- Ground in customer job-to-be-done and measurable gains.
- Keep it language that resonates with target segments.

## Variants
- "One-liner" ( ultra concise )
- "Messaging pillar" (broader positioning statements)
