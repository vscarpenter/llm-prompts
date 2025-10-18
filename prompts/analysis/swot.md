---
domain: analysis
version: 1.1
author: llm-prompts
---

# SWOT Analysis Generator

## Prompt
```
Create a SWOT analysis for [TOPIC/DECISION/PROJECT].

Context: [PROVIDE BACKGROUND]

Format as:
Strengths: (internal, positive)
Weaknesses: (internal, negative)
Opportunities: (external, positive)
Threats: (external, negative)

Be specific and actionable rather than generic.
```

## Output Format
- A concise 4-quadrant matrix with bullet points per quadrant.
- Optional prioritization notes for top items.

## Sample Output
```markdown
Strengths:
- Brand recognition
- Scalable tech

Weaknesses:
- Limited sales coverage
- Dependence on a single supplier

Opportunities:
- New geographic markets
- Strategic partnerships

Threats:
- Competitive paywalls
- Regulatory changes
```

## Tips / Notes
- Tie SWOT items to strategic actions.
- Use data to back up claims where possible.

## Variants
- "SWOT with action items" (include specific next steps for each quadrant)
- "Competitive SWOT" (compare against specific competitors)
- "TOWS Matrix" (match external opportunities/threats with internal strengths/weaknesses)
- "Weighted SWOT" (assign importance scores to each item)
