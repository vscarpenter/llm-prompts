# Translate Code Between Languages

## Prompt
> Translate this code from {{source_language}} to {{target_language}}, preserving logic while using idiomatic patterns for the target language.
>
> Source code:
> ```{{source_language}}
> {{code_snippet}}
> ```
>
> **Translation requirements:**
> - Use {{target_language}} best practices and idioms
> - Replace libraries with equivalent {{target_language}} packages
> - Include necessary imports/dependencies
> - Add comments explaining translation choices where idioms differ
> - Maintain error handling and edge case logic

## Tips / Notes
- Specify framework: "use Express.js" or "use Flask framework"
- For type systems: "add TypeScript types" or "include Python type hints"
- Specify version: "use Python 3.12+" or "ES2023 features"
- Add context: "this is part of a REST API" or "this runs in a browser"

## Variants
- "Translate but make it more idiomatic" (not literal translation)
- "Include setup instructions and dependency list"
- "Create side-by-side comparison with explanations"
- "Translate and modernize" (use latest language features)
