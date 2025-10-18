---
domain: planning
version: 1.1
author: llm-prompts
---

# Feature Breakdown

## Prompt
> You are a technical lead breaking down a feature into implementable tasks.
>
> Feature to implement: {{feature_description}}
>
> Break this down into a structured implementation plan:
>
> ## Overview
> Brief summary of what we're building and why
>
> ## Technical Approach
> High-level strategy (2-3 sentences)
>
> ## Tasks
>
> ### Phase 1: Foundation
> 1. [Task] - What needs to be done, why it's needed
> 2. [Task] - Acceptance criteria for completion
>
> ### Phase 2: Core Implementation
> 1. [Task] - Specific deliverable
> 2. [Task] - Dependencies on other tasks
>
> ### Phase 3: Integration & Polish
> 1. [Task] - Final integration work
> 2. [Task] - Edge cases and error handling
>
> ## Testing Strategy
> - Unit tests needed
> - Integration tests needed
> - Manual testing checklist
>
> ## Risks & Unknowns
> - Potential blockers or uncertainties
> - What needs investigation before starting
>
> Each task should be completable in 2-4 hours. Be specific about what "done" looks like. Flag dependencies between tasks.

## Tips / Notes
- Use for features that will take multiple days to implement
- Adjust phase names based on your workflow
- Include database migrations, API changes, UI work as separate tasks
- Don't over-plan - details will emerge during implementation

## Variants
- Bug Investigation Plan - Break down steps to diagnose and fix a complex bug
- Refactoring Plan - Structure incremental refactoring with no-downtime approach
