---
domain: communication
version: 1.1
author: llm-prompts
---

# Slack Announcement

## Prompt
> Write a concise Slack announcement for a team update.
>
> Topic: "{{topic}}"
> Key message: "{{message}}"
> Audience: "{{channel}}"
> Action needed: "{{yes_or_no}}"
>
> **Output:** Short, friendly message with a call to action.

## Output Format
- 1–2 paragraphs, suitable for a Slack channel.
- Include a CTA.

## Sample Output
```markdown
Hey @channel, quick update on {{topic}}: {{message}}. Please review and share your thoughts in the thread.
```

## Tips / Notes
- Keep it brief; use emoji sparingly.

## Variants
- "Channel-specific" (tone tuned to #team-updates, #announcements)
- "Casual rollout" (informal, friendly)
