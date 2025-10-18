---
domain: communication
version: 1.1
author: llm-prompts
---

# Meeting Agenda

## Prompt
> Generate a concise meeting agenda for a given purpose.
>
> Purpose: "{{purpose}}"
> Attendees: "{{attendees}}"
> Duration: "{{duration}}" minutes
> Key topics: "{{topics}}"
>
> **Output:** Agenda with time allocations and notes.

## Output Format
- Clear agenda with time blocks and owners
- Optional pre-read and action items

## Sample Output
```markdown
0:00-0:10 Welcome & Objectives (Owner)
0:10-0:30 Topic 1 (Owner)
0:30-0:40 Decision Point / Next Steps (Owner)
```

## Tips / Notes
- Share pre-reading material ahead of time
- Capture decisions and owners

## Variants
- "Strategic planning" (vision and roadmap)
- "1-on-1 agenda" (manager/employee check-in)
- "All-hands agenda" (company-wide update)
- "Workshop agenda" (interactive activities)
