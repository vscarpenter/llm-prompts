# Code Review Assistant

## Prompt
> Perform a thorough code review of the following code with constructive feedback.
>
> Code to review:
> ```{{language}}
> {{code_snippet}}
> ```
>
> Focus areas: "{{all|security|performance|readability|best_practices}}"
> Context: "{{code_purpose_and_context}}"
>
> **Code review structure:**
>
> **1. Summary Assessment**
> - Overall code quality (1-5 stars)
> - Key strengths (2-3 things done well)
> - Critical issues (must-fix before merge)
>
> **2. Detailed Feedback by Category:**
>
> **Correctness & Logic:**
> - ✅ [What's working correctly]
> - ⚠️ [Potential bugs or edge cases not handled]
> - 💡 [Logic improvements]
>
> **Security:**
> - ✅ [Security measures in place]
> - 🔴 [Vulnerabilities found]
> - 💡 [Security improvements]
>
> **Performance:**
> - ✅ [Efficient approaches]
> - ⚠️ [Performance concerns]
> - 💡 [Optimization opportunities]
>
> **Readability & Maintainability:**
> - ✅ [Clear, well-named variables/functions]
> - ⚠️ [Confusing or unclear sections]
> - 💡 [Readability improvements]
>
> **Best Practices & Patterns:**
> - ✅ [Good patterns used]
> - ⚠️ [Anti-patterns or code smells]
> - 💡 [Better approaches]
>
> **Testing:**
> - Current test coverage assessment
> - Additional test scenarios needed
>
> **3. Specific Line-by-Line Comments:**
> Line X: [Comment]
> Line Y: [Comment]
>
> **4. Suggestions (with code examples):**
> Instead of:
> ```{{language}}
> {{original_code}}
> ```
> Consider:
> ```{{language}}
> {{improved_code}}
> ```
> Reason: [Why this is better]
>
> **5. Questions for Author:**
> - [Question about design choice]
> - [Question about requirement]
>
> **6. Approval Status:**
> - ✅ Approve (ship it!)
> - ⚠️ Approve with comments (non-blocking suggestions)
> - 🔴 Request changes (must address issues before merge)

## Tips / Notes
- Specify review depth: "quick scan," "detailed review," "security-focused audit"
- Add tone: "mentoring tone for junior dev" or "peer-level feedback"
- Request focus: "only critical issues" or "include style suggestions"
- For learning: "explain the reasoning behind each suggestion"

## Variants
- "Security-focused review" (focus on vulnerabilities, OWASP top 10)
- "Performance review" (algorithmic complexity, optimization opportunities)
- "Style/lint review" (code standards and formatting)
- "Architectural review" (design patterns, separation of concerns)
