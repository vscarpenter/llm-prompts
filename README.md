# llm-prompts

> A curated library of high-utility prompts for writing, coding, strategizing, teaching — and more.

---

## 🚀 Why this exists

- The real power of LLMs lies in the *prompt*, not the model.
- **79+ battle-tested prompts** covering 14 domains — from code reviews to business strategy.
- Save time. Avoid prompt trial & error. Start with proven templates.
- Build a shared, evolving "prompt baseline" across teams or the community.
- Open-source and LLM-agnostic — works with Claude, GPT-4, Gemini, and more.
- Encourage contributions: your favorite prompt could help thousands.

---

## 📂 Structure / Organization

```
/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── CLAUDE.md
└── prompts/
    ├── analysis/         (8 prompts)
    ├── business/         (6 prompts)
    ├── communication/    (8 prompts)
    ├── creative/         (5 prompts)
    ├── data/             (5 prompts)
    ├── developer/        (10 prompts)
    ├── documentation/    (3 prompts)
    ├── learning/         (7 prompts)
    ├── meetings/         (4 prompts)
    ├── planning/         (3 prompts)
    ├── product/          (5 prompts)
    ├── productivity/     (5 prompts)
    ├── summarization/    (2 prompts)
    └── writing/          (8 prompts)
```

### 📊 Analysis (8 prompts)
Strategic frameworks and decision-making tools
- `2x2_matrix.md` - Create 2x2 positioning matrices
- `competitive_analysis.md` - Analyze competitive landscape
- `decision_matrix.md` - Weighted decision-making framework
- `pros_cons_list.md` - Structured pros/cons evaluation
- `risk_assessment.md` - Identify and evaluate risks
- `root_cause_analysis.md` - 5 Whys and cause analysis
- `swot.md` - SWOT analysis framework
- `tradeoff.md` - Evaluate tradeoffs and alternatives

### 💼 Business (6 prompts)
Strategy, planning, and business development
- `business_model_canvas.md` - BMC framework
- `competitive_analysis.md` - Market positioning
- `customer_interview_guide.md` - Interview questions
- `elevator_pitch.md` - Concise pitch creation
- `go_to_market_plan.md` - GTM strategy
- `value_proposition.md` - Value prop development

### 💬 Communication (8 prompts)
Professional communication and messaging
- `advanced_editing.md` - Deep editing and rewriting
- `difficult_conversation.md` - Handle tough conversations
- `executive_email.md` - C-level communication
- `feedback_note.md` - Constructive feedback
- `meeting_agenda.md` - Structured agendas
- `presentation_outline.md` - Presentation structure
- `slack_announcement.md` - Team announcements
- `status_update.md` - Project status reports

### 🎨 Creative (5 prompts)
Ideation and creative content
- `analogy_generator.md` - Create analogies
- `brainstorm.md` - Structured brainstorming
- `name_generator.md` - Product/company names
- `story_structure.md` - Narrative frameworks
- `tagline_slogan.md` - Marketing copy

### 📈 Data (5 prompts)
Data analysis and research planning
- `chart_recommendation.md` - Visualization selection
- `data_analysis_plan.md` - Analysis frameworks
- `hypothesis_generator.md` - Research hypotheses
- `research_questions.md` - Question formulation
- `sql_explainer.md` - Explain SQL queries

### 👨‍💻 Developer (10 prompts)
Software development and documentation
- `api_documentation.md` - API docs generation
- `architecture_decision_record.md` - ADR templates
- `code_review.md` - Code review feedback
- `debug_help.md` - Debugging assistance
- `explain_code.md` - Code explanation
- `generate_tests.md` - Test generation
- `naming_things.md` - Variable/function naming
- `readme_generator.md` - README creation
- `refactor.md` - Code refactoring
- `translate_language.md` - Language translation

### 📄 Documentation (3 prompts)
Technical documentation and decision records
- `adr.md` - Architecture Decision Records
- `api_documentation.md` - API endpoint documentation
- `readme_generator.md` - README file generation

### 📚 Learning (7 prompts)
Education and knowledge acquisition
- `explain_concept.md` - Concept explanations
- `explain_like_im_5.md` - Simplified explanations
- `flashcards.md` - Study flashcards
- `learning_path.md` - Curriculum creation
- `quiz_generator.md` - Assessment creation
- `study_guide.md` - Study materials
- `technical_concept_breakdown.md` - Detailed technical explanations

### 🤝 Meetings (4 prompts)
Meeting facilitation and collaboration
- `decision_log.md` - Document decisions and rationale
- `one_on_one_agenda.md` - 1-on-1 meeting structure
- `retrospective.md` - Sprint/project retrospectives
- `technical_discussion.md` - Technical discussion facilitation

### 📋 Planning (3 prompts)
Project and task planning
- `estimation.md` - Task complexity and timeline estimation
- `feature_breakdown.md` - Break features into tasks
- `technical_design.md` - Technical design documents

### 🎯 Product (5 prompts)
Product management frameworks
- `feature_prioritization.md` - Feature ranking
- `jobs_to_be_done.md` - JTBD framework
- `prd_template.md` - Product requirements
- `user_persona.md` - Persona development
- `user_story.md` - User story creation

### ⚡ Productivity (5 prompts)
Personal and team productivity
- `daily_plan.md` - Time-blocked schedules tied to must-win outcomes and energy
- `okr_generator.md` - OKRs with initiatives, owners, and measurement cadence
- `prioritization.md` - Framework scoring with risk, dependency, and parking lot views
- `retrospective.md` - Data-driven retro with accountable follow-ups
- `task_breakdown.md` - Phased WBS with acceptance criteria and comms plan

### 📝 Summarization (2 prompts)
Content condensation and synthesis
- `article_summary.md` - Article summaries
- `book_summary.md` - Book summaries

### ✍️ Writing (8 prompts)
Content creation and editing
- `blog_post_outline.md` - Blog structure
- `cold_email.md` - Outreach emails
- `grammar_check.md` - Grammar and spelling
- `linkedin_post_from_notes.md` - LinkedIn content
- `meeting_notes_to_actions.md` - Extract action items
- `press_release.md` - PR writing
- `rewrite_style.md` - Style and tone adjustment
- `technical_documentation.md` - Technical writing

---

**Total: 79+ prompts across 14 domains**

- `prompts/…` — grouped by domain (writing, dev, analysis, business, etc.)
- each `.md` is one prompt (with sections for **"Prompt Text"**, **"Explanation / Tips for Use"**, **"Variants / Customization"**)
- `CONTRIBUTING.md` — how to add your prompt, formatting rules, review process
- `CLAUDE.md` — instructions for Claude Code when working with this repository

---

## ✅ Sample Prompt File (e.g. `prompts/writing/rewrite_style.md`)

```markdown
# Rewriting for Tone / Clarity / Style

## Prompt

> You are a professional editor. Rewrite the following text to improve clarity, tone, grammar, and flow, while preserving the original meaning.
> Text: “{{input_text}}”

## Tips / Notes

- Adjust “tone” (formal, casual, friendly) by appending a clause.
- Use “preserve meaning” to avoid hallucination.
- Limit output length if you only want part of it.

## Variants

- “Rewrite but simpler (grade‑level 8)”
- “Rewrite for CMO / high-level exec, more persuasive”
- “Produce 3 versions, then your pick with rationale”
```

---

## 📣 Contribution Guide (`CONTRIBUTING.md`)

- Pick an existing domain or propose a new one
- Use the prompt file template
- Include your name / GitHub handle
- Add test / example inputs + outputs
- Keep things **clear, minimal, modular**
- Submit a PR — maintainers will review and merge

---

## 📜 License & Code of Conduct

- Use a permissive license (e.g. MIT)
- Include a **Code of Conduct** (e.g. Contributor Covenant)
- Encourage respectful collaboration

---

## 🧪 How to Use It

1. Clone the repo
2. Browse `prompts/` by domain
3. Copy the prompt you need, plug your `{{input}}`
4. Tweak role, tone, or constraints as needed
5. Add your own prompt via pull request

---

## 🚀 Roadmap & Wishlist

- [ ] Web UI / prompt playground
- [ ] Prompt versioning / evaluation
- [ ] Industry-specific prompt collections (fintech, health, edu, legal)
- [ ] Community gallery & featured prompts
- [ ] Prompt testing & quality metrics
- [ ] Multi-language prompt translations
- [ ] Integration examples with popular LLM APIs
- [ ] Video tutorials and prompt engineering guides

---

## 💬 Acknowledgments & Inspiration

Thank you to the broader LLM and prompt engineering community for inspiration. This repository is built on the collective knowledge of practitioners who've shared their best practices and frameworks.

---

## 📬 Stay in Touch

- LinkedIn: https://www.linkedin.com/in/vinnycarpenter/
- Website: https://vinny.dev/
- Feel free to ⭐ the repo, clone it, and share your favorite prompts.
