---
domain: communication
version: 1.1
author: llm-prompts
---

# Advanced Editing Assistant

## Prompt
> Provide advanced editing for professional writing, focusing on clarity, tone, and impact.
>
> Text: "{{input_text}}"
>
> **Editing guidelines:**
>- Grammar/spelling: Fix errors, follow AP style, use Oxford commas
>- Sentence structure: Keep under 25 words, use active voice, replace jargon
>- Flow: Smooth transitions, vary sentence length, cut redundancies
>- Paragraphs: 4-5 sentences max, strong topic sentences, blank lines between
>- Word choice: Replace weak verbs with vivid ones
>- Tone: Friendly, confident, gender-neutral, professional
>
> **Output:** Polished text only (no tracked changes unless requested)

## Output Format
- Edited text only
- Short rationale for major edits

## Sample Output
```markdown
Edited Text: ...
Notes: Adjusted tone to be more concise; clarified sentence 2.
```

## Tips / Notes
- Request track changes: "show before/after with explanations"
- Adjust formality: "make more casual" or "make more formal"
- Add "follow Chicago Manual" instead of AP style
- For technical writing: "preserve technical terminology"

## Variants
- "Edit for ESL audience" (simpler vocabulary, clearer structure)
- "Edit for technical accuracy" (preserve technical terms)
- "Aggressive editing" (cut 30% of words while keeping meaning)
- "Show tracked changes with explanations for each edit"