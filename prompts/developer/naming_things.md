# Naming Assistant

## Prompt
> Suggest clear, descriptive names for this code element.
>
> What needs naming: "{{variable|function|class|file|project|api_endpoint}}"
> Purpose: "{{what_it_does}}"
> Context: "{{code_context}}"
> Language/Framework: "{{language}}"
> Current name (if any): "{{current_name}}"
>
> **Naming recommendations:**
>
> **1. Top Recommendations** (3-5 options)
> - `{{name_option_1}}` - [Why this works, what it communicates]
> - `{{name_option_2}}` - [Why this works, what it communicates]
> - `{{name_option_3}}` - [Why this works, what it communicates]
>
> **2. Naming Rationale**
> - **Clarity**: How well the name describes its purpose
> - **Consistency**: How it fits with existing codebase conventions
> - **Length**: Balance between descriptiveness and brevity
> - **Conventions**: Language/framework naming standards followed
>
> **3. Anti-patterns to Avoid**
> - ❌ `{{bad_name_example}}` - [Why this is unclear/misleading]
> - ❌ `{{another_bad_example}}` - [Why to avoid]
>
> **4. Naming Convention Guidelines** (for this language/framework)
> - Function naming: [Convention, e.g., camelCase, describes action]
> - Variable naming: [Convention, e.g., descriptive nouns]
> - Class naming: [Convention, e.g., PascalCase, singular nouns]
> - Constants: [Convention, e.g., UPPER_SNAKE_CASE]
>
> **5. Related Names** (if part of a family)
> - If there's `{{name}}`, consider naming related items:
>   - `{{related_name_1}}`
>   - `{{related_name_2}}`

## Tips / Notes
- Specify style: "follow Google style guide," "match existing codebase style"
- Add context: "part of authentication system," "for internal utility"
- Request variations: "suggest both short and long form names"
- For refactoring: "existing name is `{{old_name}}`, suggest better alternative"

## Variants
- "Project naming" (product, repository, or codebase names)
- "API endpoint naming" (RESTful conventions, resource-oriented)
- "Database naming" (tables, columns, indexes)
- "Refactor renaming" (improve existing unclear names)
