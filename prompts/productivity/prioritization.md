# Task Prioritization

## Prompt
> Help me prioritize these tasks using a structured framework.
>
> Tasks: "{{task_list}}"
> Context: "{{constraints_or_goals}}"
> Energy availability / personal constraints: "{{energy_windows|obligations}}"
> Prioritization method: "{{eisenhower|ice_score|rice|moscow|custom}}"
>
> **Output structure:**
> 1. **Scoring table** (Task | Framework-specific metrics | Effort | Impact | Confidence/Energy fit)
> 2. **Prioritized list** (ranked by importance/urgency)
> 3. **Framework rationale** (why each task is positioned where it is)
> 4. **Action recommendations** (what to do first, what to delegate, what to defer/drop)
> 5. **Risks & Dependencies** (call out blockers, upstream/downstream impacts)
> 6. **Parking lot** (tasks to revisit later with review cadence)
> 7. **Timeline suggestion** (when to tackle each priority tier)
>
> **Common frameworks:**
> - **Eisenhower Matrix**: Urgent/Important quadrants
> - **ICE Score**: Impact × Confidence × Ease
> - **RICE**: Reach × Impact × Confidence / Effort
> - **MoSCoW**: Must have, Should have, Could have, Won't have

## Tips / Notes
- Specify constraints: "must complete in 2 weeks," "team of 3 people," "budget of $10k"
- Add goals: "maximize revenue impact," "improve user satisfaction," "reduce technical debt"
- Include context tags for personal vs. professional work and required energy levels
- Request batching/theme days for similar tasks to reduce context switching
- Request specific framework or let LLM recommend: "suggest best prioritization method"
- For teams: "consider dependencies between tasks"

## Variants
- "Quick triage" (immediate/this week/this month/someday)
- "Value vs. effort matrix" (2x2 plot of all tasks)
- "Dependency-aware prioritization" (order by what unblocks other work)
- "Weighted scoring" (custom criteria with importance weights)
