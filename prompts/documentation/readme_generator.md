# README Generator

## Prompt
> You are a technical writer creating clear, professional README documentation.
>
> Based on this project: {{project_description}}
>
> Generate a README.md with the following sections:
>
> # {{Project Name}}
>
> ## Overview
> Brief (2-3 sentence) description of what this project does and why it exists.
>
> ## Features
> - Key capabilities (bullet points)
>
> ## Installation
> Step-by-step setup instructions
>
> ## Usage
> Basic examples showing how to use the main functionality
>
> ## Configuration
> Environment variables or config options (if applicable)
>
> ## Development
> How to run locally, run tests, contribute
>
> ## License
> License type
>
> Use clear, concise language. Include code examples where helpful. Assume the reader is a developer familiar with the tech stack.

## Tips / Notes
- Paste in your package.json, main files, or describe your project
- Remove sections that don't apply (e.g., Configuration if none needed)
- Add badges (build status, version) after generation if desired
- Keep it focused on what users need to get started

## Variants
**Minimal README** - Just Overview, Installation, and Usage sections for simple projects

**Library README** - Focus on API documentation and examples instead of installation steps
