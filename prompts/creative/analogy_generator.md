---
domain: creative
version: 1.1
author: llm-prompts
---

# Analogy Generator

## Prompt
> Create compelling analogies to explain this complex concept in accessible terms.
>
> Concept to explain: "{{concept}}"
> Target audience: "{{audience}}"
> Context: "{{why_they_need_to_understand}}"
>
> **Analogy requirements:**
> - Familiar reference point (everyday experience)
> - Clear mapping (how elements correspond)
> - Illuminates key insight
> - Appropriate for audience
> - Doesn't oversimplify or mislead
>
> **Deliverables:**
> 1. **3-5 analogy options** from different domains:
>    - Physical/mechanical analogy
>    - Human/social analogy
>    - Nature/biological analogy
>    - Technology/everyday object analogy
>
> 2. **Extended explanation** for best analogy:
>    - Setup (introduce familiar concept)
>    - Mapping (show correspondences)
>    - Insight (what the analogy reveals)
>    - Limitations (where analogy breaks down)

## Output Format
- Analogy in one to two sentences plus a short explanation.

## Sample Output
```markdown
"Explaining a distributed system is like coordinating a team of musicians: each service plays its own part, and orchestration ensures harmony."
```

## Tips / Notes
- Specify domain: "use cooking analogies," "use sports references," "use nature examples"
- Add constraints: "for non-technical audience," "for executives," "for children"
- Request sophistication: "simple surface analogy" or "deep structural metaphor"
- For teaching: "build from simple to complex analogy"

## Variants
- "Visual metaphor" (describe an image or diagram that represents the concept)
- "Extended metaphor" (develop one analogy in depth with sub-mappings)
- "Analogy chain" (series of analogies building understanding progressively)
- "Cultural-specific analogies" (tailored to specific cultural contexts)
