# Refactor for Performance and Readability

## Prompt
> Refactor the following code to improve quality while preserving functionality.
>
> Code:
> ```{{language}}
> {{code_snippet}}
> ```
>
> **Refactoring priorities:**
> 1. **Readability** - Clear variable names, reduce nesting, add helpful comments
> 2. **Maintainability** - Extract repeated logic, single responsibility functions
> 3. **Performance** - Optimize algorithms, reduce unnecessary operations
>
> **Output:**
> 1. Refactored code with inline comments explaining changes
> 2. Summary of improvements made
> 3. Performance impact (if applicable)

## Tips / Notes
- Specify priorities: "prioritize readability over performance" or "focus on performance optimization"
- Add constraints: "don't change function signatures" or "maintain backward compatibility"
- Specify style guide: "follow Airbnb style guide" or "use PEP 8"
- For legacy code: "modernize without breaking existing functionality"

## Variants
- "Refactor for testability" (dependency injection, pure functions)
- "Modernize code" (use latest language features like async/await, destructuring)
- "Refactor for specific design pattern" (Strategy, Factory, Observer, etc.)
- "Extract reusable utilities/helpers from this code"
