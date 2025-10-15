# Technical Documentation Writer

## Prompt
> Create clear, comprehensive technical documentation for this feature, API, or system.
>
> Subject: "{{what_to_document}}"
> Audience: "{{developers|end_users|internal_team}}"
> Type: "{{api|user_guide|architecture|reference}}"
> Context: "{{technical_details}}"
>
> **Documentation structure:**
>
> **Overview** (1-2 paragraphs)
> - What this is
> - Why it exists / what problem it solves
> - Key capabilities
>
> **Getting Started** (Quick start guide)
> - Prerequisites
> - Installation / setup steps
> - "Hello World" example
> - Expected output
>
> **Core Concepts** (if needed)
> - Key terminology
> - Architecture overview
> - How components interact
>
> **Detailed Guide:**
>
> **[Feature/Endpoint 1]:**
> - Description
> - Parameters (name, type, required/optional, description, default)
> - Example request
> - Example response
> - Error codes and meanings
>
> **[Feature/Endpoint 2]:**
> - [Same structure]
>
> **Common Use Cases:**
> - Use case 1: [Scenario and code example]
> - Use case 2: [Scenario and code example]
>
> **Troubleshooting:**
> - Common error 1: [Cause and solution]
> - Common error 2: [Cause and solution]
>
> **Best Practices:**
> - Recommendation 1
> - Recommendation 2
>
> **Reference:**
> - Complete parameter list
> - Configuration options
> - Limits and constraints
>
> **Additional Resources:**
> - Related documentation
> - Tutorials
> - Support channels

## Tips / Notes
- Specify format: "Markdown," "OpenAPI spec," "inline code comments," "README"
- Add examples: "include code examples in {{language}}"
- Request style: "follow Google developer docs style" or "conversational tone"
- For APIs: "include curl examples and SDK code snippets"

## Variants
- "API documentation" (REST/GraphQL endpoint reference)
- "User guide" (end-user feature documentation with screenshots)
- "Architecture documentation" (system design and data flow diagrams)
- "README generator" (project overview, setup, usage, contributing)
