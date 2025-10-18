---
domain: creative
version: 1.1
author: llm-prompts
---

# Name Generator

## Prompt
> Generate creative, memorable names for the following concept.
>
> What needs naming: "{{product|company|feature|project}}"
> Description: "{{what_it_does}}"
> Target audience: "{{audience}}"
> Tone/vibe: "{{professional|playful|technical|aspirational}}"
>
> **Naming criteria:**
> - Memorable and easy to pronounce
> - Relevant to purpose or benefit
> - Distinctive (stands out from competitors)
> - Domain/trademark friendly (if applicable)
> - Works across cultures (no unintended meanings)
>
> **Deliverables:**
> - 20-30 name options organized by style
> - Top 5 recommendations with rationale
> - Domain availability notes (if .com available, suggest it)
> - Potential taglines for top names
## Output Format
- List of names with one-line rationale each.
## Sample Output
```markdown
1) NovaSync — conveys speed and harmony
```
## Tips / Notes
- Specify naming style: "descriptive," "abstract," "invented words," etc.
- Add constraints: "must include 'data'" or "must start with A"
- Request variations: "provide 5 variations of the top 3 names"
- For brands: "test for negative connotations in other languages"
## Variants
- "Startup name generator" (focus on .com availability)
- "Feature codename" (internal project names)
- "Character/persona names" (for marketing personas)
- "Name + tagline combo" (integrated naming and positioning)
