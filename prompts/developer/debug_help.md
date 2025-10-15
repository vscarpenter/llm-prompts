# Debug Helper

## Prompt
> Help me debug this error and suggest solutions.
>
> Error message:
> ```
> {{error_message}}
> ```
>
> Code that's failing:
> ```{{language}}
> {{code_snippet}}
> ```
>
> Context: "{{what_you_were_trying_to_do}}"
> Environment: "{{language_version|framework|os}}"
> What you've tried: "{{debugging_steps_taken}}"
>
> **Debugging assistance:**
>
> **1. Error Explanation**
> - What this error means in plain English
> - Most common causes of this error
> - Why it's happening in your specific case
>
> **2. Root Cause Analysis**
> - Likely source of the problem (line/function identified)
> - Why the code is producing this error
> - Related issues to check
>
> **3. Solution (Step-by-Step)**
>
> **Fix #1: [Most likely solution]**
> ```{{language}}
> {{corrected_code}}
> ```
> - What changed and why
> - Why this fixes the issue
>
> **Fix #2: [Alternative approach]** (if applicable)
> ```{{language}}
> {{alternative_code}}
> ```
> - When to use this instead
>
> **4. Verification Steps**
> - How to test that the fix works
> - What to look for to confirm it's resolved
> - Edge cases to test
>
> **5. Prevention**
> - How to avoid this error in the future
> - Debugging tips for similar issues
> - Linting rules or guards to add
>
> **6. Additional Debugging**
> - If this doesn't work, try: [Next debugging steps]
> - Related areas to investigate
> - Logging/breakpoints to add

## Tips / Notes
- Specify urgency: "production issue, need quick fix" or "learning opportunity, explain deeply"
- Add constraints: "can't change function signature" or "must maintain backward compatibility"
- Request depth: "just the fix" vs "teach me how to debug this type of error"
- For learning: "explain the underlying concept that causes this"

## Variants
- "Stack trace analysis" (parse complex error stack and identify root cause)
- "Performance debugging" (slow code, memory leaks, bottlenecks)
- "Logic debugging" (incorrect output, behavior not as expected)
- "Debugging checklist" (systematic approach to isolate the problem)
