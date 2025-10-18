---
domain: creative
version: 1.1
author: llm-prompts
---

# Story Structure Generator

## Prompt
> Outline a story structure for a narrative concept.
>
> Topic: "{{topic}}"
> Genre: "{{genre}}"
> Audience: "{{audience}}"
> Length: "{{length}}" sentences
> Themes: "{{themes_to_explore}}"
>
> **Story structure (Three-Act or Hero's Journey):**
>
> **Act 1: Setup**
> - Opening image/hook
> - Protagonist introduction (wants, fears, flaws)
> - Inciting incident (disrupts normal world)
> - Point of no return
>
> **Act 2: Confrontation**
> - Rising action and obstacles
> - Midpoint reversal (stakes raised)
> - Dark night of the soul
> - Character transformation begins
>
> **Act 3: Resolution**
> - Climax (final confrontation)
> - Resolution
> - Character arc completion
> - Closing image
>
> **Additional elements:**
> - B-plot/subplots
> - Supporting characters and their arcs
> - Key scenes/moments
+
+## Output Format
+- Provide a beat-by-beat outline or a full three-act structure depending on length.
+
+## Sample Output
+```markdown
+Act 1: Setup ...
+Act 2: Confrontation ...
+Act 3: Resolution ...
+```
+
+## Tips / Notes
+- Specify structure: "Hero's Journey" or "Three-Act" etc.
+- Add genre conventions and any required twists.
+- Focus on character arcs and turning points.
+
+## Variants
+- "Character development arc" (internal transformation focus)
+- "Scene-by-scene outline" (beat sheet)
+- "Parallel storylines" (multiple POVs/timelines)
+- "Short story structure" (compressed three-act for 5-10 pages)
