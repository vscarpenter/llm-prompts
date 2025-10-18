---
domain: meetings
version: 1.1
author: llm-prompts
---

# Sprint/Project Retrospective

## Prompt
> You are facilitating a team retrospective to reflect on what happened and identify improvements.
>
> Context: {{retro_context}} (e.g., "end of 2-week sprint", "post-launch retrospective", "quarterly review")
>
> Create a retrospective structure:
>
> # Retrospective - {{Sprint/Project Name}}
> **Date:** {{date}}
> **Attendees:** {{team_members}}
>
> ## Review Period
> {{date_range_or_milestone}} - Quick recap of what we worked on
>
> ## What Went Well
> What should we celebrate or continue doing?
> -
> -
>
> ## What Didn't Go Well
> What caused friction, delays, or frustration?
> -
> -
>
> ## Lessons Learned
> What did we learn that we didn't know before?
> -
> -
>
> ## Action Items
> Specific, actionable improvements we'll implement:
> 1. **{{Action}}** - Owner: {{name}}, By: {{date}}
> 2. **{{Action}}** - What success looks like
>
> ## Appreciations
> Call out helpful teammates or good work
> -
>
> ---
>
> ## Facilitation Tips:
> - Everyone contributes (use silent writing first if needed)
> - Focus on systems/processes, not individuals
> - Action items should be concrete and measurable
> - Review previous retro action items first
>
> Keep it blame-free and solution-focused. The goal is continuous improvement, not finger-pointing.
>
## Output Format
- A polished retrospective with sections for What Went Well, What Didn\'t Go Well, Actions, and Follow-up.
## Variants
- "Incident Retrospective" - Focus on timeline, root cause, prevention measures
- "Project Post-Mortem" - Deeper analysis for major projects with metrics
- "Team Health Check" - Focus on team dynamics and processes
