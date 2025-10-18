---
domain: product
version: 1.1
author: llm-prompts
---

# Product Requirements Document (PRD)

## Prompt
> Create a comprehensive Product Requirements Document for this feature or product.
>
> Product/Feature: "{{name}}"
> Problem: "{{problem_statement}}"
> Users: "{{target_users}}"
> Goals: "{{business_and_user_goals}}"
>
> **PRD Structure:**
>
> **1. Overview**
> - Problem statement (what problem are we solving?)
> - Goals and success metrics
> - Target users and personas
>
> **2. User Stories & Use Cases**
> - Primary use cases (happy paths)
> - Edge cases
> - User scenarios
>
> **3. Requirements**
> - **Functional requirements** (what it must do)
> - **Non-functional requirements** (performance, security, scalability)
> - **User interface requirements**
> - **Data requirements**
>
> **4. Out of Scope**
> - What we're explicitly NOT building (manage expectations)
>
> **5. Success Metrics**
> - How we'll measure success (KPIs)
> - Target metrics and timeline
>
> **6. Technical Considerations**
> - Dependencies and integrations
> - Technical constraints
> - Security and privacy requirements
>
> **7. Launch Plan**
> - Rollout strategy
> - Timeline and milestones
> - Risks and mitigation
## Output Format
- A complete PRD document in Markdown with sections and structured content.
## Sample Output
```markdown
# PRD Title
## Overview
...
```
## Tips / Notes
- Specify depth: "one-pager," "detailed PRD," "epic-level overview"
- Add audience: "for engineering," "for stakeholders," "for design"
- Request sections: "include competitive analysis," "include user research findings"
- For new products: "include go-to-market section"
## Variants
- "Lean PRD" (one-page)
- "Technical spec from PRD" (translate to engineering requirements)
- "PRD review checklist" (evaluate an existing PRD)
- "Feature brief" (lightweight version for small features)
