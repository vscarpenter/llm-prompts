---
domain: learning
version: 1.1
author: llm-prompts
---

# Explain Concept (ELI5)

## Prompt
> Explain the following concept in simple, accessible terms that anyone can understand.
>
> Concept: "{{concept}}"
> Context (optional): "{{context}}"
>
> **Explanation structure:**
> 1. **Simple definition** (one sentence, no jargon)
> 2. **Why it matters** (real-world relevance)
> 3. **How it works** (step-by-step or analogy)
> 4. **Concrete example** (relatable scenario)
> 5. **Common misconceptions** (what people get wrong)
>
> **Tone:** Conversational, encouraging, non-condescending
> **Avoid:** Jargon, circular definitions, overwhelming detail
+
+## Output Format
+- Simple explanation with optional examples or visuals.
+
+## Sample Output
+```markdown
+Concept: Quantum Superposition
+Explanation: ...
+```
+
+## Tips / Notes
+- Audience level: "ELI5", "explain like a student" etc.
+- Learning goal: what to enable next
+- Request analogies: cooking analogy, everyday tech
+
+## Variants
+- "ELI5 format" (extremely simple, playful)
+- "Explain with visual metaphor" (image/diagram)
+- "Socratic explanation" (guided questions)
+- "Build-up explanation" (start simple, add complexity)
