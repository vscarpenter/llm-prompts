---
domain: learning
version: 1.1
author: llm-prompts
---

# Flashcard Generator

## Prompt
> Generate effective flashcards for memorization and active recall from this content.
>
> Topic: "{{topic}}"
> Content: "{{source_material}}"
>
> **Flashcard requirements:**
> - Front: Clear, specific question or prompt
> - Back: Concise answer (1-3 sentences)
> - Create 15-25 cards covering key concepts
> - Mix card types: definitions, examples, applications, connections
> - Avoid yes/no questions (require recall, not recognition)
> 
> **Format:**
>```
>Card 1
>Front: [Question]
>Back: [Answer]
>```
 
## Tips / Notes
- Specify focus: "definitions," "applications," "comparisons"
- Add difficulty levels: "tag as beginner/intermediate/advanced"
- Request card types: "include cloze deletion cards" or "include image description cards"
- For languages: "include pronunciation hints" or "include example sentences"

## Variants
- "Anki format" (for Anki import)
- "Quizlet format" (tab-separated for Quizlet)
- "Cloze deletion cards" (fill-in-the-blank)
- "Reverse cards" (bidirectional)
