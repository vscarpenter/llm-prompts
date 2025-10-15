# API Documentation Generator

## Prompt
> You are a technical writer creating clear API documentation.
>
> Document the following API endpoint: {{endpoint_description}}
>
> Use this structure:
>
> ## {{HTTP Method}} {{Endpoint Path}}
>
> **Description:** What this endpoint does (1-2 sentences)
>
> **Authentication:** Required auth method (if any)
>
> **Request**
>
> Path Parameters:
> - `{{param}}` (type) - description
>
> Query Parameters:
> - `{{param}}` (type, optional/required) - description
>
> Request Body:
> ```json
> {
>   "example": "request"
> }
> ```
>
> **Response**
>
> Success (200):
> ```json
> {
>   "example": "response"
> }
> ```
>
> **Error Responses**
> - 400 Bad Request - Invalid input
> - 401 Unauthorized - Missing or invalid auth
> - 404 Not Found - Resource doesn't exist
>
> **Example Request**
> ```bash
> curl -X {{METHOD}} \
>   {{base_url}}{{endpoint}} \
>   -H "Authorization: Bearer {{token}}" \
>   -d '{{request_body}}'
> ```
>
> Include realistic examples. Be specific about required vs optional fields. Document common error cases.

## Tips / Notes
- Paste in your route handler code or OpenAPI spec for best results
- Group related endpoints together
- Include rate limits, pagination details if applicable
- Update examples to use your actual domain/naming conventions

## Variants
**GraphQL Documentation** - Document queries, mutations, and types with example queries

**WebSocket Documentation** - Document events, message formats, and connection lifecycle
