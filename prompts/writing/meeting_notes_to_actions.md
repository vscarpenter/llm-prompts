---
domain: writing
version: 1.1
author: llm-prompts
---

# Meeting Notes to Action Items

## Prompt
> Extract clear action items and key decisions from these meeting notes.
>
> Meeting: "{{meeting_title}}"
> Date: "{{date}}"
> Attendees: "{{participants}}"
> Raw notes: "{{meeting_notes}}"
>
> **Structured output:**
>
> **Meeting Summary** (2-3 sentences)
> [High-level takeaway - what was accomplished or decided]
>
> **Key Decisions Made:**
> 1. [Decision] - Rationale: [why]
> 2. [Decision] - Rationale: [why]
>
> **Action Items:**
> | Action | Owner | Due Date | Priority | Status |
> |--------|-------|----------|----------|--------|
> | [Specific task] | [Name] | [Date] | High/Med/Low | Not started |
>
> **Open Questions / Blockers:**
> - [Question that needs answering]
> - [Blocker that needs resolving]
>
> **Key Discussion Points:**
> - [Topic discussed]
> - [Important context or insights]
>
> **Follow-up Needed:**
> - Next meeting: [When and what to cover]
> - Information to gather before then
>
> **Parking Lot** (topics tabled for later):
> - [Topic to revisit]
+
+## Tips / Notes
+- Specify format: "for team sync," "for client meeting," "for executive briefing"
+- Add urgency: "flag urgent action items"
+- Request clarity: "convert vague notes into specific, measurable actions"
+- For distribution: "format for Slack/email/project management tool"
+
+## Variants
+- "Executive summary" (condensed to 5 bullet points for leadership)
+- "Action-only email" (just the action items for quick reference)
+- "Decision log" (focus on capturing decisions with context)
+- "Customer meeting notes" (include customer feedback themes and requests)
