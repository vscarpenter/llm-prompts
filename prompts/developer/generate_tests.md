# Generate Unit Tests

## Prompt
> Create comprehensive unit tests for this code:
>
> ```{{language}}
> {{code_snippet}}
> ```
>
> **Framework:** {{test_framework}} (or auto-detect)
>
> **Coverage Requirements:**
>
> ✅ **Test Categories:**
> - Happy path (normal inputs → expected outputs)
> - Edge cases (boundaries, empty, null, zero, max values)
> - Error cases (invalid inputs, exceptions, type errors)
> - All branches (every if/else, switch case, loop condition)
> - State changes and side effects
>
> 📝 **Test Name Format:**
> `test_[function]_[when/with_condition]_[expected_result]`
>
> 🎯 **For Each Test:**
> ```
> // GIVEN: Setup and context
> // WHEN: Action being tested
> // THEN: Expected outcome
> ```
>
> 🔧 **Include:**
> - Descriptive test names and comments
> - Setup/teardown methods
> - Mocked dependencies
> - Assertion messages for debugging
> - Parameterized tests for similar cases
> - Both positive and negative tests
>
> 📊 **Deliverables:**
> 1. Complete test file ready to run
> 2. Coverage summary comment
> 3. Run command example
> 4. Any required test fixtures or helpers
>
> **Focus on:** Behavior over implementation, isolated tests, meaningful failures, 100% branch coverage

## Tips / Notes
- Specify test framework if not auto-detecting: "use Jest," "use pytest," "use JUnit"
- Add coverage target: "aim for 90% code coverage" or "focus on critical paths only"
- For legacy code: "add tests before refactoring to ensure behavior preservation"
- Request specific test types: "focus on integration tests" or "unit tests only"

## Variants
- "Generate TDD-style tests" (write tests first, then implementation)
- "Property-based tests" (use frameworks like Hypothesis, fast-check)
- "Snapshot tests" (for UI components or data structures)
- "E2E test scenarios" (end-to-end user flows instead of unit tests)
