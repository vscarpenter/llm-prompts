---
domain: product
version: 1.1
author: llm-prompts
---

# User Story

## Prompt
> Write well-structured user stories with acceptance criteria for this feature.
>
> Feature: "{{feature_description}}"
> User type: "{{persona_or_role}}"
> Goal: "{{what_user_wants_to_achieve}}"
> Context: "{{background_or_constraints}}"
>
> **User story format:**
>
> **As a** [type of user]
> **I want** [goal or desire]
> **So that** [benefit or value]
>
> **Acceptance Criteria:**
> - **Given** [initial context/state]
> - **When** [action taken]
> - **Then** [expected outcome]
> - (Repeat for each scenario: happy path, edge cases, error states)
>
> **Definition of Done:**
> - [ ] Checklist of completion requirements
> - [ ] Testing requirements
> - [ ] Documentation needs
>
> **Additional details:**
> - Priority: High/Medium/Low
> - Story points estimate: X
> - Dependencies: [related stories]
## Output Format
- A set of user stories with acceptance criteria in Gherkin-like syntax.
## Sample Output
```markdown
As a user, I want to ...
```
## Tips / Notes
- Specify format: "Gherkin syntax," "traditional user story," "job story format"
- Add granularity: "epic level," "feature level," "task level"
- Request details: "include wireframes," "include API requirements"
- For technical stories: "system-level stories"
## Variants
- "Epic breakdown" (large feature split into multiple user stories)
- "Job story format" (When [situation], I want to [motivation], so I can [outcome])
- "User story mapping" (organize stories by user journey)
- "Story refinement" (refine rough idea into ready-to-develop story)
