---
domain: writing
version: 1.1
author: llm-prompts
---

# Grammar and Spell Check

## Prompt
> You are a professional proofreader. Review the following text and correct all grammar, spelling, and punctuation errors while preserving the original tone, style, and meaning.
>
> Text: "{{input_text}}"
>
> **Output format:**
> 1. Corrected text
> 2. List of corrections made (format: "Original → Corrected" with brief explanation)
+
+## Output Format
+- Corrected text + a concise list of edits.
+- Optional notes on tone/concision.
+
+## Sample Output
+```markdown
+Edited Text: ...
+Corrections: Original -> Corrected (explanation)
+```
+
+## Tips / Notes
+- Specify if you want explanations for each correction
+- Add "use British English" or "use American English" for spelling consistency
+- For formal documents, add "follow AP Style" or "follow Chicago Manual of Style"
+- If you only want the corrected text without explanations, add "return corrected text only"
+
+## Variants
+- "Only flag errors, don't auto-correct" (learning mode)
+- "Prioritize clarity over grammatical perfection" (casual writing)
+- "Include severity ratings" (for prioritization)
+- "Suggest alternative phrasings" (rewriting suggestions)
