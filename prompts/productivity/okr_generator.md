# OKR Generator

## Prompt
> Create Objectives and Key Results (OKRs) for the following goal.
>
> Goal/Mission: "{{goal}}"
> Time period: "{{quarter|year}}"
> Team/Role: "{{team_or_role}}"
> Measurement cadence: "{{weekly|monthly|mid-quarter}}"
> Data sources available: "{{crm|analytics|surveys|manual_tracking}}"
>
> **OKR structure:**
>
> **Objective**: [Qualitative, inspirational, time-bound goal]
>
> **Key Results** (3-5 measurable outcomes):
> | KR | Metric | Baseline | Target | Indicator Type | Owner |
> |----|--------|----------|--------|----------------|-------|
> | KR1 | [Metric description] | [Current value] | [Target value] | [Leading/Lagging] | [Role] |
> | KR2 | [Metric description] | [Current value] | [Target value] | [Leading/Lagging] | [Role] |
> | KR3 | [Metric description] | [Current value] | [Target value] | [Leading/Lagging] | [Role] |
>
> **Initiatives / Projects** (per KR)
> - Initiative A: [Project name] → Supports KR#
> - Resources needed: [People, budget, tools]
>
> **Measurement Plan**
> - Cadence: [Weekly/Monthly]
> - Source: [System/report]
> - Confidence & risks: [High/Medium/Low, gaps to close]
>
> **Guidelines:**
> - Objectives: Ambitious but achievable, clear direction
> - Key Results: Specific metrics, measurable, time-bound, tag leading vs. lagging indicators
> - Include baseline, target, and owner for each KR
> - Aim for 70% achievement as success (stretch goals)
> - Flag data gaps or assumptions that threaten measurability

## Tips / Notes
- Specify scope: "company-level," "team-level," "individual contributor"
- Add context: "we're a startup in growth mode" or "enterprise with mature product"
- Request alignment: "align with company OKRs: [list parent OKRs]"
- Supply baseline sources: "pull last quarter ARR from finance dashboard"
- Ask for confidence level and mitigation plan if targets feel at-risk
- For cascading: "create team OKRs that support this organizational objective"

## Variants
- "Individual OKRs" (personal professional development goals)
- "OKR tree" (company → team → individual alignment)
- "OKR health check" (evaluate existing OKRs for quality)
- "Mid-cycle OKR adjustment" (revise based on progress and learnings)
