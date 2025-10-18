---
domain: analysis
version: 1.1
author: llm-prompts
---

# Risk Assessment

## Prompt
> Identify and evaluate risks for this decision or project.
>
> Topic/Project: "{{topic}}"
> Scope: "{{scope}}"
> Stakeholders: "{{stakeholders}}"
> Time horizon: "{{time horizon}}"
> > **Assess:** probability, impact, detectability, and mitigation.
>
> **Output:** Risk register with prioritization and mitigations.

## Output Format
- Risk register table with risk, probability, impact, severity, mitigations, owner.
- Optional heat-map visualization (ASCII or Markdown table).

## Sample Output
```markdown
| Risk | Probability | Impact | Severity | Mitigation | Owner |
|------|-------------|--------|----------|------------|-------|
| Data breach | High | Severe | Critical | Encrypt at rest, rotate keys | SecOps |
```

## Tips / Notes
- Distinguish knowns, unknowns, and assumptions.
- Include trigger conditions and residual risk.

## Variants
- "Threat modeling" (STRIDE)  
- "Quantitative risk scoring" (Monte Carlo etc.)
