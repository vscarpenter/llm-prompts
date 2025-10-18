---
domain: data
version: 1.1
author: llm-prompts
---

# Data Analysis Plan

## Prompt
> Create a structured plan for analyzing this dataset to answer specific questions.
>
> Dataset description: "{{data_description}}"
> Research question: "{{question_or_hypothesis}}"
> Goal: "{{what_decision_this_informs}}"
> Available tools: "{{sql|python|r|excel|tableau}}"
>
> **Analysis plan structure:**
>
> **1. Question refinement:**
> - Primary question (specific, measurable)
> - Sub-questions to explore
> - Success criteria (what would make this analysis valuable)
>
> **2. Data exploration:**
> - Data quality checks (missing values, outliers, duplicates)
> - Descriptive statistics (distributions, ranges, counts)
> - Initial visualizations to understand data shape
>
> **3. Analysis approach:**
> - Statistical methods to use (and why)
> - Segmentation strategy (how to break down data)
> - Key metrics to calculate
> - Comparisons to make (time periods, groups, benchmarks)
>
> **4. Validation strategy:**
> - How to check if findings are reliable
> - Sensitivity analysis (what assumptions matter most)
> - Statistical significance tests (if applicable)
>
> **5. Deliverables:**
> - Visualizations to create
> - Key insights to surface
> - Recommendations format
> - Audience and communication approach
>
+## Tips / Notes
+- Specify analysis type: "exploratory," "confirmatory," "predictive modeling"
+- Add constraints: "analysis must complete in 2 days," "use only SQL"
+- Request specific methods: "include hypothesis testing," "use regression analysis"
+- For presentations: "include executive summary approach"
+
+## Variants
+- "Exploratory data analysis (EDA) checklist" (systematic exploration steps)
+- "A/B test analysis plan" (specific to experiment analysis)
+- "Time series analysis approach" (for temporal data)
+- "Cohort analysis framework" (user behavior over time)
