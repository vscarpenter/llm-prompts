---
domain: data
version: 1.1
author: llm-prompts
---

# Hypothesis Generator

## Prompt
> Generate testable hypotheses based on this observation, question, or research goal.
>
> Observation/Question: "{{observation}}"
> Domain: "{{field_or_context}}"
> Available data: "{{data_description}}"
> Type: "{{null_hypothesis|alternative|directional}}"
>
> **Hypothesis structure:**
>
> **1. Null Hypothesis (H₀):**
> [Statement of no effect or no relationship]
>
> **2. Alternative Hypothesis (H₁ or Hₐ):**
> [Statement of expected effect or relationship]
>
> **3. Variables:**
> - **Independent variable(s)**: What we're manipulating/comparing
> - **Dependent variable(s)**: What we're measuring
> - **Control variables**: What we need to hold constant
>
> **4. Operational definitions:**
> - How each variable will be measured
> - Units and scales
>
> **5. Testability:**
> - Proposed method to test (experiment, correlation analysis, A/B test, etc.)
> - Sample size requirements
> - Statistical test to use
> - What would confirm or reject the hypothesis
>
> **6. Assumptions:**
> - What must be true for this hypothesis to make sense
> - Potential confounding factors
>
> **7. Implications:**
> - If hypothesis is supported: [what it means]
> - If hypothesis is rejected: [what it means]
>
+## Output Format
+- List of 5-10 hypotheses with rationale and test method.
+
+## Sample Output
+```markdown
+H1: ...
+```
+
+## Tips / Notes
+- Specify hypothesis type: "causal","correlational","comparative"
+- Add rigor level: "academic" or "business decision" 
+- Request multiples: "generate 3-5 competing hypotheses"
+- For experiments: "include power analysis requirements"
+
+## Variants
+- "Hypothesis refinement" (make vague hypotheses more specific)
+- "Competing hypotheses" (multiple explanations for same observation)
+- "Hypothesis to experiment design" (from hypothesis to full protocol)
+- "Bayesian hypothesis framing" (prior beliefs and how evidence updates them)
