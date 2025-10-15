# Chart Type Recommendation

## Prompt
> Recommend the best data visualization type for this data and insight.
>
> Data description: "{{data_structure}}"
> Message/insight: "{{what_you_want_to_show}}"
> Audience: "{{who_will_see_this}}"
> Context: "{{dashboard|presentation|report|social_media}}"
>
> **Visualization recommendation:**
>
> **1. Recommended chart type:**
> [Chart name] (e.g., bar chart, line chart, scatter plot, heat map)
>
> **2. Rationale:**
> - Why this chart type fits the data
> - Why it communicates the insight effectively
> - What makes it right for this audience
>
> **3. Design specifications:**
> - Axes: What goes on X and Y
> - Encoding: Use of color, size, shape
> - Labels: What text to include
> - Title: Suggested chart title that conveys insight
>
> **4. Alternative options:**
> - 2nd choice chart type (and when to use it)
> - 3rd choice (and trade-offs)
>
> **5. Anti-recommendations:**
> - Chart types to avoid (and why they'd be misleading)
>
> **6. Implementation notes:**
> - Tool-specific tips (Excel, Tableau, Python, etc.)
> - Common pitfalls to avoid

## Tips / Notes
- Specify goal: "show comparison," "show trend over time," "show distribution," "show relationship"
- Add constraints: "must work in black and white," "for color-blind accessibility"
- Request specifics: "include data-to-ink ratio optimization"
- For dashboards: "suggest interactive elements"

## Variants
- "Dashboard design recommendation" (multiple charts working together)
- "Infographic structure" (visual storytelling with multiple data points)
- "Chart makeover" (improve an existing visualization)
- "Accessible visualization" (optimize for screen readers and color-blindness)
