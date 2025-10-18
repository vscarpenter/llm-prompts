---
domain: learning
version: 1.1
author: llm-prompts
---

# Study Guide

## Prompt
> Create a comprehensive study guide from the following material to help students master the content.
>
> Subject: "{{subject}}"
> Source material: "{{content}}"
> Exam/goal: "{{exam_or_goal}}"
>
> **Study guide structure:**
> 1. **Key concepts** (main ideas with definitions)
> 2. **Important terms** (vocabulary with explanations)
> 3. **Core principles** (rules, theories, frameworks)
> 4. **Relationships** (how concepts connect)
> 5. **Practice questions** (5-10 questions with answers)
> 6. **Memory aids** (mnemonics, acronyms, tricks)
>
> **Format:** Organized by topic, scannable, study-friendly

## Output Format
- Structured study guide organized by topic with concise sections.

## Sample Output
```markdown
Module 1: ...
```

## Tips / Notes
- Specify exam type: "for multiple choice test," "for essay exam," etc.
- Add difficulty: "foundational concepts" or "advanced applications"
- Request specific formats: "Cornell notes" or "outline format"
- Time constraint: "cramming in 2 hours" vs "deep understanding over 2 weeks"

## Variants
- "One-page cheat sheet" (ultra-condensed reference)
- "Spaced repetition schedule" (review plan)
- "Active recall questions" (no answers)
- "Visual study guide" (diagrams, mind maps)
