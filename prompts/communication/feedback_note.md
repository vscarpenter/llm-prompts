---
domain: communication
version: 1.1
author: llm-prompts
---

# Feedback Note

## Prompt
> Write constructive feedback that is specific, balanced, and actionable.
>
> Situation: "{{context}}"
> Behavior to address: "{{behavior}}"
> Impact: "{{impact}}"
>
> **Feedback structure (SBI Framework):**
> 1. **Situation:** When/where this occurred (specific, recent)
> 2. **Behavior:** Observable actions (not judgments or assumptions)
> 3. **Impact:** How it affected you, the team, or results
> 4. **Forward path:** Specific suggestions or questions for improvement
>
> **Tone:** Respectful, empathetic, growth-focused
> **Format:** 3-5 sentences, include positive framing where appropriate
+
+## Output Format
+- Polished feedback note with 1-2 actionable next steps.
+
+## Sample Output
+```markdown
+Hi {{recipient}},
+
+Feedback: {{feedback}}.
+Next steps: 1) ..., 2) ...
+Best,
+{{sender}}
+```
+
+## Tips / Notes
+- For positive feedback, be specific about what to keep doing
+- For critical feedback, focus on behavior not personality
+- End with a question: "How do you see it?" or "What support do you need?"
+- Specify relationship: "for peer," "for direct report," "for manager"
+
+## Variants
+- "360 feedback format" (structured with rating + comments)
+- "Radical candor approach" (direct but caring)
+- "Growth-focused feedback" (emphasize potential and development)
+- "Peer feedback" (collaborative, equals-based tone)
