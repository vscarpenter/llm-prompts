---
domain: analysis
version: 1.1
author: llm-prompts
---

# Competitive Analysis Framework

## Prompt
> Analyze the competitive landscape for this product, feature, or market.
>
> Your product: "{{product}}"
> Market/Category: "{{market}}"
> Competitors: "{{competitor_names}}"
> Focus: "{{features|pricing|positioning|go_to_market}}"
> Audience: "{{who_needs_this_analysis}}"
>
> **Competitive Analysis:**
>
> **1. Market Overview**
> - Market size and growth
> - Key trends shaping the market
> - Customer segments
> - Entry barriers
>
> **2. Competitive Landscape Map**
>
> **Market Leaders** (high market share, established):
> - Company A: [Brief description, market position]
> - Company B: [Brief description, market position]
>
> **Challengers** (growing fast, innovative):
> - Company C: [Brief description, market position]
>
> **Niche Players** (specialized, focused):
> - Company D: [Brief description, market position]
>
> **Your Position**: [Where you fit in this landscape]
>
> **3. Competitor Deep Dive**
>
> **Competitor: [Company A]**
>
> **Overview:**
> - Founded: [Year]
> - Size: [Employees, revenue if public]
> - Funding: [Amount raised, investors]
> - Market share: [Estimate]
>
> **Value Proposition:**
> [How they position themselves]
>
> **Target Customers:**
> [Who they serve, primary segments]
>
> **Strengths:**
> - ✅ [What they do exceptionally well]
> - ✅ [Another strength]
> - ✅ [Another strength]
>
> **Weaknesses:**
> - ❌ [Gap or limitation]
> - ❌ [Customer complaint]
> - ❌ [Area where they lag]
>
> **Product/Features:**
> - Core features: [List key capabilities]
> - Recent launches: [New products/features]
> - Roadmap signals: [What they're building next]
>
> **Pricing:**
> - Model: [Subscription, usage-based, etc.]
> - Entry price: [$X/month]
> - Enterprise pricing: [Range or approach]
> - Discounting strategy: [Annual deals, volume discounts]
>
> **Go-to-Market:**
> - Customer acquisition: [How they get customers]
> - Sales model: [Self-serve, sales-led, hybrid]
> - Marketing channels: [Primary channels]
> - Partnership strategy: [Key partners]
>
> **Customer Feedback:**
> - Common praises: [What users love]
> - Common complaints: [Pain points from reviews]
> - NPS/satisfaction: [If available]
>
> **Strategic Moves:**
> - Recent acquisitions: [Companies acquired]
> - Key hires: [Notable executives joined]
> - Funding/IPO: [Recent capital events]
>
> [Repeat structure for each competitor]
>
> **4. Feature Comparison Matrix**
>
> | Feature | Your Product | Competitor A | Competitor B | Competitor C |
> |---------|--------------|--------------|--------------|--------------|
> | Feature 1 | ✅ Full | ✅ Full | ⚠️ Limited | ❌ None |
> | Feature 2 | ✅ Full | ⚠️ Limited | ✅ Full | ⚠️ Beta |
> | Feature 3 | ⚠️ Roadmap | ✅ Full | ✅ Full | ❌ None |
> | Pricing (entry) | $X | $Y | $Z | $W |
> | Free tier | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
>
> **5. Positioning Map**
>
> ```
> High Price
>     │
>     │  [Competitor A]
>     │                    [Your Product]
> ────┼──────────────────────────────── Enterprise ← → SMB
>     │          [Competitor B]
>     │
>     │ [Competitor C]
> ```
>
> **6. SWOT vs. Competition**
>
> **Your Strengths** (competitive advantages):
> - [What you do better than everyone]
>
> **Your Weaknesses** (competitive disadvantages):
> - [Where competitors beat you]
>
> **Market Opportunities** (gaps to exploit):
> - [Underserved segments or needs]
>
> **Competitive Threats**:
> - [What could hurt your position]
>
> **7. Win/Loss Analysis**
>
> **Why customers choose you over competitors:**
> - Reason 1
> - Reason 2
>
> **Why customers choose competitors over you:**
> - Reason 1
> - Reason 2
>
> **8. Strategic Recommendations**
>
> **Differentiation strategy:**
> - [How to position uniquely]
>
> **Feature gaps to close:**
> - [ ] Priority 1
> - [ ] Priority 2
>
> **Defensive moats to build:**
> - [How to make your position defensible]
>
> **Offensive opportunities:**
> - [Where to attack competitors' weaknesses]
>
+## Output Format
+- Provide a concise executive summary of the landscape and top 3 strategic moves.
+- Deliver a structured battle-card style output for quick use in sales.
+
+## Sample Output
+```markdown
+Topic: Example Market
+Top Moves: 1) Parity pricing, 2) Target niche segment, 3) Improve onboarding
+```
+
+## Tips / Notes
+- Specify depth: "quick competitive scan" or "comprehensive market analysis"
+- Add focus: "feature parity analysis," "pricing strategy," "market positioning"
+- Request format: "executive summary" or "detailed battle cards for sales"
+- For strategy: "include blue ocean opportunities (uncontested market space)"
+
+## Variants
+- "Competitive battle cards" (sales enablement, how to win vs each competitor)
+- "Market positioning analysis" (perceptual maps, strategic positioning)
+- "Pricing competitive analysis" (deep dive on pricing and packaging)
+- "Feature gap analysis" (what to build to reach feature parity or leapfrog)
