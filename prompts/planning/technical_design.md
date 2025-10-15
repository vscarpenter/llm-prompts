# Technical Design Document

## Prompt
> You are a software architect creating a technical design document.
>
> System to design: {{system_description}}
>
> Create a concise technical design with these sections:
>
> # {{System Name}} - Technical Design
>
> ## Problem Statement
> What problem are we solving? Why does this need to be built?
>
> ## Goals & Non-Goals
> **Goals:**
> - What this system will do
>
> **Non-Goals:**
> - What this explicitly won't handle (to prevent scope creep)
>
> ## Proposed Solution
>
> ### Architecture Overview
> High-level components and how they interact (describe or use simple diagram)
>
> ### Key Components
> 1. **Component Name** - Responsibility, key interfaces
> 2. **Component Name** - Technologies used, why chosen
>
> ### Data Model
> Key entities and relationships (if applicable)
>
> ### API Design
> Critical endpoints or interfaces (high-level)
>
> ## Alternative Approaches Considered
> What other solutions did we evaluate? Why did we choose this approach?
>
> ## Security Considerations
> Authentication, authorization, data protection measures
>
> ## Performance Considerations
> Expected load, scalability approach, caching strategy
>
> ## Deployment & Operations
> How this will be deployed, monitored, and maintained
>
> ## Open Questions
> What still needs to be decided or investigated?
>
> ## Timeline Estimate
> Rough phases and duration
>
> Keep it concise - this should be readable in 10 minutes. Focus on decisions that are hard to change later.

## Tips / Notes
- Use for new systems or major architectural changes
- Review with team before implementation starts
- Update as design evolves, but keep history of major decisions
- Link to ADRs for specific technical decisions

## Example Usage
Replace `{{system_description}}` with:
- "Real-time notification system for user activities"
- "Multi-tenant authentication service"
- "Data pipeline for processing customer analytics"
