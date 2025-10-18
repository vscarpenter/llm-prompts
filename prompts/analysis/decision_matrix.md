---
domain: analysis
version: 1.1
author: llm-prompts
---

# Decision Matrix (Weighted Scoring)

## Prompt
> Create a weighted decision matrix to objectively compare options.
>
> Decision: "{{what_you're_deciding}}"
> Options: "{{option_1}}, {{option_2}}, {{option_3}}..."
> Criteria: "{{decision_factors}}"
> Context: "{{constraints_and_goals}}"
>
> **Decision Matrix:**
>
> **1. Define Criteria & Weights**
>
> | Criteria | Weight (%) | Rationale |
> |----------|------------|-----------|
> | Cost | 25% | Budget is tight |
> | Time to implement | 20% | Need quick wins |
> | Scalability | 20% | Must handle growth |
> | User experience | 15% | Important but not critical |
> | Technical complexity | 10% | Team capability factor |
> | Maintenance burden | 10% | Long-term consideration |
> 
> **2. Scoring System**
> - 5 = Excellent (exceeds expectations)
> - 4 = Good (meets expectations well)
> - 3 = Acceptable (meets minimum requirements)
> - 2 = Poor (below expectations)
> - 1 = Unacceptable (does not meet requirements)
> 
> **3. Score Each Option**
> 
> | Criteria | Weight | Option A | Score | Weighted | Option B | Score | Weighted | Option C | Score | Weighted |
> |----------|--------|----------|-------|----------|----------|-------|----------|----------|-------|----------|
> | Cost | 25% | $50k | 4 | 1.00 | $80k | 2 | 0.50 | $65k | 3 | 0.75 |
> | Time to implement | 20% | 3 months | 3 | 0.60 | 2 months | 4 | 0.80 | 4 months | 2 | 0.40 |
> | Scalability | 20% | High | 5 | 1.00 | Medium | 3 | 0.60 | High | 4 | 0.80 |
> | [etc.] |  |  |  |  |  |  |  |  |  |  |
> | **TOTAL** | **100%** |  |  | **X.XX** |  |  | **Y.YY** |  |  | **Z.ZZ** |
> 
> **4. Results**
> 
> **Rankings:**
> 1. Option [X] - Score: [#.##]
> 2. Option [Y] - Score: [#.##]
> 3. Option [Z] - Score: [#.##]
> 
> **5. Analysis**
> 
> **Winner: Option [X]**
> - Strengths: [Why it scored well]
> - Weaknesses: [Where it fell short]
> - Best for: [Scenarios where this is the right choice]
> 
> **Runner-up: Option [Y]**
> - When to choose instead: [Conditions where this becomes better]
> 
> **6. Sensitivity Analysis**
> 
> **What if we changed the weights?**
> - If cost weight increased to 40%: [How rankings change]
> - If time weight decreased to 10%: [How rankings change]
> 
> **What if scores changed?**
> - If Option B's scalability improved to 5: [New total score]
> 
> **7. Recommendation**
> 
> **Recommended choice**: [Option X]
> 
> **Rationale**: [Why this is the best choice given the weights and context]
> 
> **Conditions for reconsidering**: [What would make us choose differently]
> 
> **Next steps**:
> - [ ] Validate assumptions for winning option
> - [ ] Prototype/pilot if needed
> - [ ] Get stakeholder buy-in
+
+## Output Format
+- Provide a ranked list of options with brief justification per item.
+- Include a small table of criteria scores per option.
+
+## Sample Output
+```markdown
+Rank 1: Option A — Justification...
+Rank 2: Option B — Justification...
+Rank 3: Option C — Justification...
+
+| Option | Criterion1 | Criterion2 | Criterion3 |
+|--------|------------|------------|------------|
+| A      | 0.9        | 0.6        | 0.8        |
+| B      | 0.7        | 0.9        | 0.5        |
+| C      | 0.5        | 0.4        | 0.7        |
+```
+
+## Tips / Notes
+- Clarify how weights map to scores.
+- Include sensitivity note if weights change slightly.
+
+## Variants
+- "Weighted criteria with probabilistic scoring" (adds confidence)
+- "Simple ranking" (no numeric scores)
