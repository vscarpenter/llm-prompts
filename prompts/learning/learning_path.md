---
domain: learning
version: 1.1
author: llm-prompts
---

# Learning Path

## Prompt
> Design a structured learning path to master the following skill or topic from beginner to proficient.
>
> Goal: "{{learning_goal}}"
> Current level: "{{beginner|intermediate|some_background}}"
> Time available: "{{time_constraint}}"
>
> **Learning path structure:**
> 1. **Prerequisites** (what you need to know first)
> 2. **Learning phases** (3-5 progressive stages)
>    - For each phase:
>      - Learning objectives (what you'll be able to do)
>      - Core concepts to master
>      - Recommended resources (types, not specific links)
>      - Practice activities
>      - Success criteria (how to know you're ready to advance)
> 3. **Capstone project** (synthesize all learning)
> 4. **Next steps** (where to go after mastery)
>
> **Estimated timeline:** Provide realistic time expectations

## Output Format
- A structured, milestone-based learning plan.

## Sample Output
```markdown
Week 1: Learn basics; Objective: ...
```

## Tips / Notes
- Specify learning style: "hands-on projects," "theoretical foundation first," etc.
- Add constraints: "free resources only," "certificate programs"
- Request specificity: "include topics" or "include example projects"
- For career goals: "align with industry standards" or "optimize for job-readiness"

## Variants
- "30-day crash course" (intensive, focused learning plan)
- "Weekend workshop curriculum" (2-day deep dive)
- "University semester outline" (15-week academic structure)
- "Self-directed learning roadmap" (milestone-based)
