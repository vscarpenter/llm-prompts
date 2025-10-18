---
domain: product
version: 1.1
author: llm-prompts
---

# Jobs to Be Done (JTBD) Analysis

## Prompt
> Analyze the "job" users are hiring this product to do using the Jobs to Be Done framework.
>
> Product/Feature: "{{product}}"
> User context: "{{user_situation}}"
> Current solutions: "{{what_users_do_now}}"
>
> **JTBD Analysis:**
>
> **1. Job Statement**
> "When [situation], I want to [motivation], so I can [desired outcome]"
>
> **2. Job Dimensions:**
> - **Functional job**: What task needs to be done?
> - **Emotional job**: How does user want to feel?
> - **Social job**: How does user want to be perceived?
>
> **3. Job Context:**
> - **Where**: Physical/digital context where job occurs
> - **When**: Timing, triggers, frequency
> - **With whom**: Others involved in getting job done
>
> **4. Success Criteria:**
> - What does success look like?
> - How do users measure whether job is done well?
> - What metrics matter to them?
>
> **5. Constraints & Obstacles:**
> - What prevents job from being done?
> - What makes current solutions inadequate?
> - What trade-offs do users make?
>
> **6. Product Implications:**
> - How should our product help get this job done?
> - What features align with this job?
> - How do we outperform current solutions?
+
+## Output Format
+- Prioritized JTBD findings with 1-2 actionable next steps per item.

## Sample Output
```markdown
Job: Improve onboarding; Action: ...
```

## Tips / Notes
- Focus on progress: "the progress user is trying to make"
- Include competing solutions: "what do users hire us vs others"
- Request job map: "break job into stages (beginning, middle, end)"
- For innovation: "identify underserved jobs or unmet needs"

## Variants
- "Job mapping" (detailed breakdown of job stages and needs at each stage)
- "Forces of progress" (push/pull forces driving users toward new solution)
- "Competing solutions analysis" (what users currently hire to get job done)
- "Outcome-driven innovation" (desired outcomes users want from job)
