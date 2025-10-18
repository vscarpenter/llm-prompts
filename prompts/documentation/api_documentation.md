---
domain: documentation
version: 1.1
author: llm-prompts
---

# API Documentation

## Prompt
> Generate API documentation for a given endpoint or service.
>
> Service: "{{service}}"
> Endpoint: "{{endpoint}}"
> Language: "{{language}}"
>
> **Output:** API spec in Markdown with endpoints, parameters, and responses.

## Output Format
- Endpoint description including parameters and responses
- Example requests/responses

## Sample Output
```markdown
### GET /items
Parameters: none
Response: 200 OK with JSON body
```

## Tips / Notes
- Keep endpoints scoped and consistent with existing API style.
