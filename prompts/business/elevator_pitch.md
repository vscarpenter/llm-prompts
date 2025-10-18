---
domain: business
version: 1.1
author: llm-prompts
---

# Elevator Pitch

## Prompt
> Craft a compelling elevator pitch for a product or idea.
>
> Product: "{{product}}"
> Audience: "{{audience}}"
> Key value: "{{value}}"
> Constraints: "{{time_limit}}" seconds
>
> **Output:** A concise pitch with a single sentence value proposition, followed by two supporting bullets.

## Output Format
- One-paragraph value proposition plus 2 bullet points.
- Optional variant: 30-second or 60-second tweaks.

## Sample Output
```markdown
We help {audience} achieve {value} by {unique mechanism}. This is better because {key benefit}. 
- Benefit 1: ...
- Benefit 2: ...
```

## Tips / Notes
- Emphasize problem, solution, and proof point quickly.
- Be explicit about target audience.

## Variants
- "Concise for formal introductions" (short and crisp)
- "Story-driven" (adds narrative context)
