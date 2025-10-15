# README Generator

## Prompt
> Create a comprehensive README file for this project.
>
> Project name: "{{project_name}}"
> Description: "{{what_the_project_does}}"
> Tech stack: "{{languages_and_frameworks}}"
> Target users: "{{developers|end_users|both}}"
> Project type: "{{library|application|framework|tool}}"
>
> **README.md Structure:**
>
> # {{Project Name}}
>
> {{Tagline or one-sentence description}}
>
> [Badges: Build Status | Coverage | Version | License | etc.]
>
> ## Overview
>
> {{2-3 paragraph description of what this project does, why it exists, and who it's for}}
>
> ## Features
>
> - ✨ Feature 1
> - 🚀 Feature 2
> - 💡 Feature 3
> - 🔒 Feature 4
>
> ## Quick Start
>
> ### Prerequisites
>
> - Node.js 18+ or Python 3.9+ or [requirements]
> - [Other dependencies]
>
> ### Installation
>
> ```bash
> npm install project-name
> # or
> pip install project-name
> ```
>
> ### Basic Usage
>
> ```{{language}}
> // Minimal working example
> import { ProjectName } from 'project-name';
>
> const instance = new ProjectName();
> instance.doSomething();
> ```
>
> ## Documentation
>
> For detailed documentation, see:
> - [API Reference](link)
> - [User Guide](link)
> - [Examples](link)
>
> ### Configuration
>
> ```{{language}}
> // Configuration example
> const config = {
>   option1: 'value',
>   option2: true
> };
> ```
>
> ### Examples
>
> **Example 1: [Use case]**
> ```{{language}}
> // Code example
> ```
>
> **Example 2: [Use case]**
> ```{{language}}
> // Code example
> ```
>
> ## Development
>
> ### Setup
>
> ```bash
> git clone https://github.com/user/project.git
> cd project
> npm install  # or pip install -e .
> ```
>
> ### Running Tests
>
> ```bash
> npm test
> # or
> pytest
> ```
>
> ### Building
>
> ```bash
> npm run build
> ```
>
> ### Project Structure
>
> ```
> project/
> ├── src/          # Source code
> ├── tests/        # Test files
> ├── docs/         # Documentation
> └── examples/     # Example usage
> ```
>
> ## Contributing
>
> Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
>
> 1. Fork the repository
> 2. Create a feature branch (`git checkout -b feature/amazing-feature`)
> 3. Commit your changes (`git commit -m 'Add amazing feature'`)
> 4. Push to the branch (`git push origin feature/amazing-feature`)
> 5. Open a Pull Request
>
> ## Roadmap
>
> - [ ] Feature planned for v1.1
> - [ ] Feature planned for v1.2
> - [ ] Long-term goal
>
> See [open issues](issues) for a full list of proposed features and known issues.
>
> ## License
>
> This project is licensed under the {{LICENSE}} License - see the [LICENSE](LICENSE) file for details.
>
> ## Acknowledgments
>
> - Inspired by [project]
> - Built with [technology]
> - Thanks to [contributors]
>
> ## Support
>
> - 📫 Issues: [GitHub Issues](link)
> - 💬 Discussions: [GitHub Discussions](link)
> - 📧 Email: support@example.com
> - 🐦 Twitter: [@handle](link)
>
> ---
>
> Made with ❤️ by [Your Name/Organization]

## Tips / Notes
- Specify project type: "open source library," "internal tool," "CLI application," "web app"
- Add sections: "include badges," "add screenshots," "include GIF demo"
- Request tone: "professional," "friendly and approachable," "minimal and technical"
- For frameworks: "include getting started tutorial"

## Variants
- "Minimal README" (essential info only, 1-page)
- "Open source README" (community focus, contribution guidelines)
- "Internal tool README" (company-specific setup, deployment)
- "Library/SDK README" (API examples, integration guides)
