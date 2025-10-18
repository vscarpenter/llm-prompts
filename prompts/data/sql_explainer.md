---
domain: data
version: 1.1
author: llm-prompts
---

# SQL Query Explainer

## Prompt
> Explain this SQL query in plain language, breaking down what it does and why.
>
> SQL Query:
> ```sql
> {{sql_query}}
> ```
>
> Database context (optional): "{{table_descriptions}}"
> Audience: "{{technical|non_technical|business_analyst}}"
>
> **Explanation structure:**
>
> **1. Query purpose** (one-sentence summary)
> What question is this query answering?
>
> **2. Step-by-step breakdown:**
> - FROM clause: Which tables we're using and how they connect
> - WHERE clause: What filters we're applying
> - JOIN logic: How tables relate to each other
> - GROUP BY: How we're aggregating data
> - HAVING: Filters applied after aggregation
> - SELECT: What columns/calculations we're returning
> - ORDER BY: How results are sorted
>
> **3. Results explanation:**
> What will the output look like? (describe structure)
>
> **4. Performance notes** (if complex):
> - Potential bottlenecks
> - Indexing recommendations
>
> **5. Plain language summary:**
> Translate the entire query into a business question

## Output Format
- Provide a clear, plain-language explanation with a short section for each bullet above.
- Include a brief performance note if relevant.

## Tips / Notes
- Specify complexity: "explain for beginners," "focus on optimization," "include execution plan analysis"
- Add context: "explain in context of monthly reporting" or "this is for a dashboard"
- Request alternatives: "suggest simpler ways to write this query"
- For learning: "explain the SQL concepts used (subqueries, CTEs, window functions, etc.)"

## Variants
- "Query optimization review" (analyze performance and suggest improvements)
- "SQL to plain English" (ultra-simple explanation for stakeholders)
- "Reverse engineer intent" (what business question prompted this query)
- "Debug SQL query" (find errors and explain fixes)
