# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a curated library of high-utility LLM prompts organized by domain. The repository contains markdown files with reusable prompts for writing, coding, analysis, communication, and summarization tasks. Each prompt is designed to be copied, customized, and used with any LLM.

## Repository Structure

```
prompts/
├── writing/           # Tone, style, grammar, LinkedIn posts
├── summarization/     # Book and article summaries
├── developer/         # Code explanation, tests, refactoring, translation
├── analysis/          # SWOT, tradeoffs, 2x2 matrices
└── communication/     # Executive emails, feedback notes, spell-check
```

## Prompt File Format

Every prompt file follows this structure:

```markdown
# [Prompt Title]

## Prompt
> The actual prompt text with {{placeholders}}

## Tips / Notes
- Usage guidelines
- Customization suggestions

## Variants (optional)
- Alternative versions for specific use cases
```

### Key Conventions
- Use `{{variable_name}}` for placeholder values (e.g., `{{input_text}}`, `{{code_snippet}}`)
- Keep prompts domain-specific and modular
- Include clear role definitions (e.g., "You are a professional editor")
- Specify output format requirements
- Provide concrete examples in Tips/Notes section

## Contributing New Prompts

When adding new prompts:

1. **Choose the right domain folder** or create a new one if needed
2. **Name the file descriptively** using snake_case (e.g., `explain_code.md`, `swot.md`)
3. **Follow the template structure** with Prompt, Tips/Notes, and optional Variants sections
4. **Make prompts actionable** - avoid generic advice, provide specific instructions
5. **Include placeholder syntax** - use `{{double_braces}}` for user inputs
6. **Test the prompt** - ensure it produces useful output before submitting

### What Makes a Good Prompt

- **Clear role/persona** - "You are a [specific expert]"
- **Specific instructions** - Define format, tone, length, structure
- **Constraints** - "while preserving the original meaning", "Be specific and actionable"
- **Output structure** - Numbered sections, headers, bullet points
- **Context placeholders** - Where users insert their content

## Repository Philosophy

This is a static collection of markdown files - no build tools, no dependencies, no configuration files. The goal is maximum simplicity and accessibility:

- Copy-paste ready prompts
- No code to run or install
- Pure markdown for easy browsing
- Version controlled for collaboration

When working with this repository, focus on:
- **Clarity over cleverness** - Prompts should be immediately understandable
- **Modularity** - Each prompt file is self-contained
- **Reusability** - Prompts work across different LLM providers
- **Conciseness** - Remove unnecessary instructions
