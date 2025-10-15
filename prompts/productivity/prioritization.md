# Task Prioritization

## Prompt
> Help me prioritize these tasks using a structured framework.
>
> Tasks: "{{task_list}}"
> Context: "{{constraints_or_goals}}"
> Prioritization method: "{{eisenhower|ice_score|rice|moscow|custom}}"
>
> **Output structure:**
> 1. **Prioritized list** (ranked by importance/urgency)
> 2. **Framework rationale** (why each task is positioned where it is)
> 3. **Action recommendations** (what to do first, what to delegate, what to defer/drop)
> 4. **Timeline suggestion** (when to tackle each priority tier)
>
> **Common frameworks:**
> - **Eisenhower Matrix**: Urgent/Important quadrants
> - **ICE Score**: Impact × Confidence × Ease
> - **RICE**: Reach × Impact × Confidence / Effort
> - **MoSCoW**: Must have, Should have, Could have, Won't have

## Tips / Notes
- Specify constraints: "must complete in 2 weeks," "team of 3 people," "budget of $10k"
- Add goals: "maximize revenue impact," "improve user satisfaction," "reduce technical debt"
- Request specific framework or let LLM recommend: "suggest best prioritization method"
- For teams: "consider dependencies between tasks"

## Variants
- "Quick triage" (immediate/this week/this month/someday)
- "Value vs. effort matrix" (2x2 plot of all tasks)
- "Dependency-aware prioritization" (order by what unblocks other work)
- "Weighted scoring" (custom criteria with importance weights)
