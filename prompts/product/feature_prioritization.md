---
domain: product
version: 1.1
author: llm-prompts
---

# Feature Prioritization

## Prompt
> Prioritize these product features using a structured framework.
>
> Features to prioritize: "{{feature_list}}"
> Product goals: "{{goals}}"
> Constraints: "{{team_size|timeline|resources}}"
> Framework: "{{rice|ice|moscow|kano|value_vs_effort}}"
>
> **Prioritization output:**
>
> **Framework application:**
> [For each feature, show scoring breakdown]
>
> Example for RICE:
> - **Reach**: How many users affected (per time period)
> - **Impact**: Value per user (0.25 = minimal, 3 = massive)
> - **Confidence**: How certain are estimates (%)
> - **Effort**: Person-months required
> - **Score**: (Reach × Impact × Confidence) / Effort
>
> **Prioritized feature list:**
> 1. Feature A (Score: X, Rationale: ...)
> 2. Feature B (Score: Y, Rationale: ...)
>
> **Roadmap recommendation:**
> - Now (Q1): [features]
> - Next (Q2): [features]
> - Later (Q3+): [features]
> - Never: [features to cut]
+
+## Output Format
+- Prioritized feature list with rationale per item.
+- Optional visual (2x2 or small table).
+
+## Sample Output
+```markdown
+1) Feature A (Score: 72) - Improves onboarding; rationale...
+```
+
+## Tips / Notes
+- Specify framework or request recommendation: select best prioritization method for early-stage.
+- Add strategic context: retention vs acquisition, debt payoff, etc.
+- Request alternatives: show prioritization with 2-3 frameworks.
+- For stakeholder buy-in: include rationale for each decision.
+
+## Variants
+- "Value vs. Effort matrix" (2x2 visualization)
+- "Kano model analysis" (classify as basic/performance/delighter)
+- "WSJF" (Weighted Shortest Job First)
+- "Theme-based prioritization" (group by themes)
