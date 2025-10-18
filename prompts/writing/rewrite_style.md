---
domain: writing
version: 1.1
author: llm-prompts
---

# Rewriting for Tone / Clarity / Style

## Prompt
> You are a professional editor. Rewrite the following text to improve clarity, tone, grammar, and flow, while preserving the original meaning.
> Text: "{{input_text}}"
+
+## Output Format
+- Edited text with optional rationale for changes.
+- If requested, provide 2-3 alternative rewrites.
+
+## Sample Output
+```markdown
+Edited Text: ...
+Rationale: ...
+```
+
+## Tips / Notes
+- Adjust tone (formal, casual, friendly) by adding a clause.
+- Use "preserve meaning" to avoid hallucination.
+- Limit output length if you only want part of it.
+- Specify target audience: "for executives," "for technical readers," "for general public"
+
+## Variants
+- "Rewrite simpler (grade 8)"
+- "Rewrite for CMO / exec, more persuasive"
+- "Produce 3 versions, then pick with rationale"
+- "Make it more concise (cut 30%)"
+- "Rewrite for a specific format: email, blog post, social media"
