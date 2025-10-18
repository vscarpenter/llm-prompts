---
domain: product
version: 1.1
author: llm-prompts
---

# User Persona Creator

## Prompt
> Create detailed, realistic user personas for this product based on research and target audience.
>
> Product: "{{product_name}}"
> Target market: "{{market_segment}}"
> Research data: "{{user_research_insights}}"
> Number of personas: "{{2-5}}"
>
> **Persona structure (for each):**
>
> **[Persona Name]** - [Role/Title]
>
> **Demographics:**
> - Age range
> - Location
> - Education
> - Income level (if relevant)
>
> **Psychographics:**
> - Values and motivations
> - Frustrations and pain points
> - Goals (personal and professional)
> - Lifestyle and behaviors
>
> **Product relationship:**
> - Use case for our product
> - How they currently solve this problem
> - Tech savviness level
> - Decision-making process
>
> **Quote:** "[Representative quote that captures their mindset]"
>
> **Goals when using our product:**
> 1. Primary goal
> 2. Secondary goal
> 3. Tertiary goal
>
> **Frustrations with current solutions:**
> 1. Main frustration
> 2. Secondary frustration
## Output Format
- A set of personas with key attributes, one per persona.
- Include a short validation checklist per persona.
## Sample Output
```markdown
Name: Jane Doe
- Role: Product Manager
- Demographics: ...
```
## Tips / Notes
- Base on data: include research findings that support each persona
- Add scenarios: include a day-in-the-life scenario
- Request focus: focus on B2B decision-makers or end users
- For validation: include persona validation checklist
## Variants
- "Proto-persona" (assumption-based before research)
- "Persona spectrum" (range of users from novice to power user)
- "Jobs-to-be-done persona" (focus on jobs they're hiring product to do)
- "Negative persona" (who we're NOT building for)
