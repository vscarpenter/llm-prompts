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

## Tips / Notes
- Specify framework or request recommendation: "suggest best prioritization method for early-stage startup"
- Add strategic context: "focusing on retention," "focusing on acquisition," "technical debt paydown"
- Request alternatives: "show prioritization with 2-3 different frameworks"
- For stakeholder buy-in: "include rationale for each decision"

## Variants
- "Value vs. Effort matrix" (2x2 visualization)
- "Kano model analysis" (classify as basic, performance, or delighter features)
- "Weighted shortest job first" (WSJF for SAFe/agile at scale)
- "Theme-based prioritization" (group features by strategic themes)
