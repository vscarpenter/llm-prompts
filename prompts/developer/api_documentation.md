# API Documentation Generator

## Prompt
> Generate comprehensive API documentation for this endpoint or SDK.
>
> API Type: "{{REST|GraphQL|gRPC|SDK}}"
> Endpoint/Method: "{{endpoint_or_method}}"
> Purpose: "{{what_it_does}}"
> Authentication: "{{auth_method}}"
>
> **API Documentation:**
>
> **Endpoint Overview**
> - **HTTP Method**: {{GET|POST|PUT|DELETE|PATCH}}
> - **Endpoint**: `{{/api/v1/resource}}`
> - **Description**: [What this endpoint does]
> - **Authentication**: [Required auth type]
> - **Rate Limits**: [Requests per minute/hour]
>
> **Request**
>
> **Headers:**
> | Header | Type | Required | Description |
> |--------|------|----------|-------------|
> | Authorization | string | Yes | Bearer token |
> | Content-Type | string | Yes | application/json |
>
> **Path Parameters:**
> | Parameter | Type | Required | Description |
> |-----------|------|----------|-------------|
> | id | integer | Yes | Resource ID |
>
> **Query Parameters:**
> | Parameter | Type | Required | Default | Description |
> |-----------|------|----------|---------|-------------|
> | page | integer | No | 1 | Page number |
> | limit | integer | No | 10 | Items per page (max 100) |
>
> **Request Body:**
> ```json
> {
>   "field1": "string",
>   "field2": 123,
>   "field3": {
>     "nested": "object"
>   }
> }
> ```
>
> **Field Descriptions:**
> - `field1` (string, required): Description of field1
> - `field2` (integer, optional): Description of field2, range 1-1000
> - `field3` (object, optional): Nested object description
>
> **Response**
>
> **Success Response (200 OK):**
> ```json
> {
>   "status": "success",
>   "data": {
>     "id": 123,
>     "created_at": "2025-01-15T10:30:00Z"
>   }
> }
> ```
>
> **Error Responses:**
>
> **400 Bad Request:**
> ```json
> {
>   "status": "error",
>   "message": "Invalid input",
>   "errors": ["field1 is required"]
> }
> ```
>
> **401 Unauthorized:**
> ```json
> {
>   "status": "error",
>   "message": "Invalid or missing authentication token"
> }
> ```
>
> **404 Not Found:**
> ```json
> {
>   "status": "error",
>   "message": "Resource not found"
> }
> ```
>
> **500 Internal Server Error:**
> ```json
> {
>   "status": "error",
>   "message": "Internal server error"
> }
> ```
>
> **Code Examples**
>
> **cURL:**
> ```bash
> curl -X POST https://api.example.com/v1/resource \
>   -H "Authorization: Bearer YOUR_TOKEN" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "field1": "value"
>   }'
> ```
>
> **JavaScript (fetch):**
> ```javascript
> const response = await fetch('https://api.example.com/v1/resource', {
>   method: 'POST',
>   headers: {
>     'Authorization': 'Bearer YOUR_TOKEN',
>     'Content-Type': 'application/json'
>   },
>   body: JSON.stringify({
>     field1: 'value'
>   })
> });
> const data = await response.json();
> ```
>
> **Python (requests):**
> ```python
> import requests
>
> response = requests.post(
>     'https://api.example.com/v1/resource',
>     headers={'Authorization': 'Bearer YOUR_TOKEN'},
>     json={'field1': 'value'}
> )
> data = response.json()
> ```

## Tips / Notes
- Specify format: "OpenAPI 3.0 spec," "Markdown," "interactive docs (Swagger)"
- Add examples: "include examples in {{languages}}"
- Request details: "include webhooks documentation" or "add SDK usage examples"
- For versioning: "include migration guide from v1 to v2"

## Variants
- "OpenAPI/Swagger spec" (machine-readable API specification)
- "GraphQL schema documentation" (queries, mutations, subscriptions)
- "SDK documentation" (library usage, class references)
- "Webhook documentation" (event types, payload structures)
