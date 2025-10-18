---
domain: data
version: 1.1
author: llm-prompts
---

# Chart Recommendation

## Prompt
> Recommend chart types for a given data set and story.
>
> Data context: "{{dataset_description}}"
> Target audience: "{{audience}}"
> Message goal: "{{goal}}"
>
> **Output:** Short chart recommendation with justification and example visuals.

## Output Format
- Chart type suggestion with a one-liner rationale.
- Optional simple ASCII visualization hint.

## Sample Output
```markdown
Recommended chart: Bar chart for categorical comparison.
Rationale: Easy comparison across categories for audience X.
```

## Tips / Notes
- Align chart with story: narrative vs analysis vs monitoring
- Ensure accessibility (color-blind friendly) and readability
