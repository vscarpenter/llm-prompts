---
domain: business
version: 1.1
author: llm-prompts
---

# Competitive Analysis Framework

## Prompt
> Analyze the competitive landscape for this market or product category.
>
> Product/Company: "{{your_product}}"
> Market: "{{market_or_category}}"
> Competitors to analyze: "{{competitor_names}}"
> Focus areas: "{{features|pricing|positioning|all}}"
>
> **Competitive analysis structure:**
>
> **1. Competitive Landscape Overview**
> - Market positioning map (where competitors sit)
> - Market share estimates
> - Category leaders vs. challengers vs. niche players
> 
> **2. Direct Competitor Analysis** (for each)
>
> **Competitor Name:**
> - **Overview**: Product description, target market, founded/size
> - **Value proposition**: How they position themselves
> - **Strengths**: What they do well
> - **Weaknesses**: Where they fall short
> - **Product features**: Key capabilities (compared to yours)
> - **Pricing**: Model and price points
> - **GTM strategy**: How they acquire customers
> - **Customer feedback**: Common praises and complaints
> - **Funding/Resources**: Financial backing and runway
> 
> **3. Competitive Matrix**
>
> | Feature/Criteria | Your Product | Competitor A | Competitor B | Competitor C |
> |------------------|--------------|--------------|--------------|--------------|
> | Price           |              |              |              |              |
> | Feature 1       |              |              |              |              |
> | Feature 2       |              |              |              |              |
> 
> **4. Market Gaps & Opportunities**
> - Underserved segments
> - Feature gaps across all competitors
> - Emerging trends competitors are missing
> 
> **5. Differentiation Strategy**
> - How to position against each competitor
> - Win themes (why customers should choose you)
> - Battle cards for sales team
> 
> **6. Threats & Response Plans**
> - Competitive threats on the horizon
> - How to defend against their moves
## Output Format
- Provide a concise executive summary and a compact, battle-card style output.
- Include a short prioritization of top differentiators.
## Sample Output
```markdown
Top Differentiators: Local data sovereignty, simpler UX, cost parity
```
## Tips / Notes
- Specify depth: "high-level overview" or "deep feature parity".
- Request competitive battle cards for sales enablement.
- Suggest blue ocean opportunities if applicable.
## Variants
- "Competitive battle cards" (sales enablement for common competitors)
- "Market positioning analysis" (strategic positioning vs. competitors)
- "Pricing competitive analysis" (deep dive on pricing and packaging)
- "Feature gap analysis" (identify gaps to close)
