---
domain: analysis
version: 1.1
author: llm-prompts
---

# Pros and Cons List

## Prompt
> Create a balanced pros and cons analysis for this decision or option.
>
> Decision/Option: "{{what_you're_considering}}"
> Context: "{{background_and_situation}}"
> Perspective: "{{who_is_deciding}}"
> Stakes: "{{what's_at_risk}}"
>
> **Pros and Cons Analysis:**
>
> **Decision**: [State the choice clearly]
## Output Format
- Provide a structured pros/cons analysis with a weighted summary.
- Include a quick risk/benefit snapshot.
## Sample Output
```markdown
Decision: Expand feature set
- Pros: Reality 1, Reality 2
- Cons: Drawback 1, Drawback 2
### Weighted Summary
- Pros Score: X
- Cons Score: Y
```
## Pros (Arguments For)
### ✅ Strong Pros (High Impact)
1. **[Benefit]**
- Details: [Explanation]
- Impact: [Who benefits, how much]
- Evidence: [Data or examples supporting this]
2. **[Benefit]**
- Details: [Explanation]
- Impact: [Who benefits, how much]
- Evidence: [Data or examples supporting this]
### ✅ Moderate Pros
3. **[Benefit]**
- Details: [Explanation]
4. **[Benefit]**
- Details: [Explanation]
### ✅ Minor Pros
5. **[Benefit]**
6. **[Benefit]**
## Cons (Arguments Against)
### ❌ Strong Cons (High Impact)
1. **[Drawback]**
- Details: [Explanation]
- Impact: [Who is affected, how severely]
- Evidence: [Data or examples supporting this]
2. **[Drawback]**
- Details: [Explanation]
- Impact: [Who is affected, how severely]
- Evidence: [Data or examples supporting this]
### ❌ Moderate Cons
3. **[Drawback]**
- Details: [Explanation]
4. **[Drawback]**
- Details: [Explanation]
### ❌ Minor Cons
5. **[Drawback]**
6. **[Drawback]**
## Weighted Summary
- Score Calculation: [How you compute the total]
## Key Considerations
**Deal-breakers**: [fatal flaws]
**Must-haves**: [critical benefits]
**Trade-offs**: [X vs Y]
## Mitigations
- Con 1 mitigation: [Strategy]
- Con 2 mitigation: [Strategy]
## Alternative Framing
**What if we don't do this?**
- Opportunity cost: [What we miss]
- Status quo consequences: [If we stay the same]
## Recommendation
**Lean**: ✅ Yes / ❌ No / ⚠️ Conditional
**Rationale**: [Why this is the right call based on the analysis]
**Conditions**: [if applicable]
- Proceed if: [Condition]
- Only if we can: [Mitigation]
**Confidence level**: [High/Medium/Low]
## Variants
- "Pre-mortem analysis" (imagine it failed, what would the cons have been)
- "Opportunity cost analysis" (what we give up by choosing this)
- "Stakeholder perspective" (pros/cons from different viewpoints)
- "Timeline-based pros/cons" (short-term vs long-term trade-offs)
