---
domain: learning
version: 1.1
author: llm-prompts
---

# Quiz Generator

## Prompt
> Create an assessment quiz to test understanding of the following material.
>
> Topic: "{{topic}}"
> Content: "{{source_material}}"
> Quiz type: "{{multiple_choice|short_answer|mixed}}"
>
> **Quiz requirements:**
> - 10-15 questions covering key concepts
> - Mix difficulty levels: 40% easy, 40% medium, 20% hard
> - Include answer key with explanations
> - Each question tests understanding, not just memorization
> - Avoid trick questions or ambiguous wording
>
> **Question types to include:**
> - Recall (what is...?)
> - Application (how would you use...?)
> - Analysis (why does...?)
> - Synthesis (what if...?)
+
+## Output Format
+- List of questions with options and correct answer.
+
+## Sample Output
+```markdown
+1) What's the main concept? A) ... B) ... C) ... | Answer: A
+```
+
+## Tips / Notes
+- Specify question format: "all multiple choice," "short answer only," or "mixed"
+- Add constraints: "no negative questions," "include 'all of the above' options"
+- Request Bloom's taxonomy levels: "focus on analysis and synthesis"
+- For practice: "include hints for each question"
+
+## Variants
+- "Exam simulation" (timed, realistic difficulty)
+- "Diagnostic quiz" (identify knowledge gaps, provide learning recommendations)
+- "Progressive quiz" (adaptive difficulty)
+- "Scenario-based assessment" (case studies with related questions)
