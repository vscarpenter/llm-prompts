---
domain: analysis
version: 1.1
author: llm-prompts
---

# Trade-Off Analysis

## Prompt
> Analyze the trade-offs between these two options with objective criteria and a recommendation.
>
> Option A: "{{option_a}}"
> Option B: "{{option_b}}"
> Context: "{{decision_context}}"
>
> **Analysis structure:**
>
> **Option A:**
> - Advantages: (3-5 specific points)
> - Disadvantages: (3-5 specific points)
> - Best suited for: (use cases/scenarios)
>
> **Option B:**
> - Advantages: (3-5 specific points)
> - Disadvantages: (3-5 specific points)
> - Best suited for: (use cases/scenarios)
>
> **Head-to-head comparison:**
>
> | Criteria | Option A | Option B | Winner |
> |----------|----------|----------|--------|
> 
> **Recommendation:**
> Choose [Option] because [key deciding factors]
> Consider Option [Other] if [specific conditions]

## Output Format
- Provide a concise head-to-head with a final recommendation.

## Sample Output
```markdown
Recommendation: Choose A due to lower cost and faster time-to-market.
```

## Tips / Notes
- Provide decision criteria: "evaluate on: cost, time, scalability, risk"
- Add constraints: "budget is $50k" or "must launch in 3 months"
- Specify perspective: "from a CTO viewpoint" or "prioritizing user experience"
- Request quantitative comparison: "include estimated costs and timelines"

## Variants
- "Multi-option comparison" (3+ options in a comparison table)
- "Devil's advocate analysis" (strongest case for each option)
- "Short-term vs long-term trade-off analysis" (immediate vs strategic impact)
- "Risk-adjusted recommendation" (include probability of success/failure)
