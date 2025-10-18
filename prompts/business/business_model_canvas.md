---
domain: business
version: 1.1
author: llm-prompts
---

# Business Model Canvas

## Prompt
> Complete a Business Model Canvas for this business idea or existing company.
>
> Business: "{{business_name}}"
> Industry: "{{industry}}"
> Stage: "{{idea|startup|growth|mature}}"
> Context: "{{additional_background}}"
>
> **Business Model Canvas (9 building blocks):**
>
> **1. Customer Segments**
> - Who are we serving?
> - Primary segment(s)
> - Niche vs. mass market
> 
> **2. Value Propositions**
> - What value do we deliver?
> - Which customer problems are we solving?
> - What benefits do we offer?
> 
> **3. Channels**
> - How do we reach customers?
> - Awareness → Evaluation → Purchase → Delivery → After-sales
> 
> **4. Customer Relationships**
> - What type of relationship does each segment expect?
> - Personal assistance / Self-service / Community / Co-creation
> 
> **5. Revenue Streams**
> - For what value are customers willing to pay?
> - How are they currently paying?
> - Pricing model (subscription, usage, freemium, etc.)
> 
> **6. Key Resources**
> - What assets are indispensable?
> - Physical / Intellectual / Human / Financial
> 
> **7. Key Activities**
> - What do we need to do to deliver our value proposition?
> - Production / Problem-solving / Platform/network
> 
> **8. Key Partnerships**
> - Who are our key partners/suppliers?
> - Strategic alliances / Joint ventures / Supplier relationships
> 
> **9. Cost Structure**
> - Most important costs?
> - Cost-driven vs. value-driven
> - Fixed vs. variable costs
## Output Format
- One-page canvas in Markdown with sections for each block.
- Include 2-4 sentence justification per block.
## Sample Output
```markdown
# Canvas for Example Venture
## Value Propositions
- Example value prop
## Customer Segments
- Example segment
```
## Tips / Notes
- Keep it concise; focus on testable assumptions.
## Variants
- "Lean Canvas style" (adapt to lean format)
