# GCP ACE Notes Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish a responsive Traditional Chinese MkDocs Material site where each Google Cloud course Markdown file renders as one course page.

**Architecture:** Markdown under `docs/` is the source of truth. MkDocs Material builds the content, client-side Chinese search index, Mermaid diagrams, responsive navigation, and print-ready static assets into `site/`; GitHub Actions validates the project and deploys that build as a GitHub Pages artifact. The repository contains no runtime server, database, credentials, generated `site/`, or fabricated terminal output.

**Tech Stack:** Python 3.13 in CI, MkDocs Material 9.7.7, Python Markdown extensions bundled with Material, Mermaid 11 from unpkg, GitHub Pages Actions, Python `unittest` acceptance tests.

## Global Constraints

- One course Markdown file produces one course page; chapters remain headings on that page.
- Course filenames use lowercase kebab-case; displayed titles retain official capitalization.
- Traditional Chinese (Taiwan) is the primary language; official Google Cloud service names remain in English.
- Preserve all supplied technical content and distinguish commands, actual output, and example output.
- Build a pure static website with no database, backend, secrets, or committed generated site.
- Only pages backed by real content appear in navigation.
- Support desktop, tablet, mobile, light/dark mode, Chinese search, tables, code copy, Mermaid overflow, printing, and keyboard focus.
- Publish on pushes to `main` with GitHub Pages artifact deployment.

## Visual System

- **Subject and job:** A focused ACE study console whose single job is helping a learner resume and navigate long Google Cloud course notes.
- **Palette:** Cloud Blue `#1a73e8`, Infrastructure Navy `#183153`, Signal Cyan `#2bb7c9`, Surface Mist `#f6f9fc`, plus Google status colors only for semantic callouts.
- **Type:** `Noto Sans TC`/system sans for reading and the restrained homepage thesis, with `Roboto Mono`/system monospace for labels, commands, and metadata.
- **Layout:** Material's three-column documentation shell, with a calm 74-character reading measure and single-column mobile collapse.
- **Signature:** A compact `LEARNING PATH / ACE` route rail on the homepage that links to the available course and never resembles a fabricated CLI command.
- **Motion:** Only subtle focus/hover movement; all transitions are removed under `prefers-reduced-motion`.

## File Map

- `mkdocs.yml`: site metadata, theme features, navigation, Markdown extensions, assets, and validation settings.
- `requirements.txt`: reproducible Python dependency pin.
- `.github/workflows/deploy-pages.yml`: test, strict build, upload, and Pages deployment.
- `.gitignore`: excludes generated output, virtual environments, and caches.
- `docs/index.md`: homepage and route rail content.
- `docs/ace/learning-path.md`: ACE reading sequence without empty-course links.
- `docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md`: supplied course, normalized as one page.
- `docs/assets/stylesheets/extra.css`: responsive reading, callouts, tables, Mermaid, print, and focus styling.
- Mermaid rendering uses Material for MkDocs 9.7.7's native custom-fence integration, including instant navigation and color-scheme support.
- `templates/course-note-template.md`: non-published reusable course template.
- `tests/test_site.py`: structural, semantic, workflow, and source-preservation acceptance checks.
- `README.md`: local Windows/WSL usage, deployment setup, next-course workflow, and troubleshooting.

---

### Task 1: Acceptance contract and project configuration

**Files:**
- Create: `tests/test_site.py`
- Create: `mkdocs.yml`
- Create: `requirements.txt`
- Create: `.gitignore`

**Interfaces:**
- Consumes: the global constraints and exact paths in this plan.
- Produces: `python -m unittest discover -s tests -v` as the repository acceptance command and `mkdocs build --strict` as the build contract.

- [ ] **Step 1: Write failing acceptance tests**

Create tests that assert the required files, one H1 in the course, normalized course path, Material navigation/features, Mermaid configuration, semantic admonitions, separated output labels, a non-published template, and secure Pages permissions.

- [ ] **Step 2: Verify the tests fail for missing site files**

Run: `python -m unittest discover -s tests -v`

Expected: failures naming missing `mkdocs.yml`, homepage, course page, workflow, template, and README.

- [ ] **Step 3: Add the minimal configuration**

Pin `mkdocs-material==9.7.7`; configure `language: zh-TW`, light/dark palettes, navigation tabs/sections/top, search highlighting/sharing, code copy/annotations, `pymdownx.superfences` Mermaid custom fence, admonitions, attributes, tables, TOC permalinks, CSS, JavaScript, and explicit navigation.

- [ ] **Step 4: Run acceptance tests**

Run: `python -m unittest discover -s tests -v`

Expected: configuration checks pass; content/workflow checks remain failing until their tasks.

### Task 2: Homepage, ACE route, and course import

**Files:**
- Create: `docs/index.md`
- Create: `docs/ace/learning-path.md`
- Create: `docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md`

**Interfaces:**
- Consumes: the source file `C:/Users/maomao/Downloads/ACE_Essential_Google_Cloud_Infrastructure_Foundation.md`.
- Produces: one navigable course page with one H1 and Chapter 1–4 as H2 headings.

- [ ] **Step 1: Verify course-content tests fail**

Run: `python -m unittest tests.test_site.CourseContentTests -v`

Expected: failure because the normalized course page does not exist.

- [ ] **Step 2: Import without deleting source content**

Copy the supplied UTF-8 Markdown, rename it to the normalized path, change the page title and all former chapter/summary H1 headings into H2, shift their child headings down one level, and retain every non-heading line.

- [ ] **Step 3: Add homepage and learning route**

Write concise Traditional Chinese copy, a primary Foundation link, current-content card, status legend, and a route rail that links only to the available course.

- [ ] **Step 4: Run course-content tests**

Run: `python -m unittest tests.test_site.CourseContentTests -v`

Expected: all course-content tests pass.

### Task 3: Responsive reading presentation and Mermaid

**Files:**
- Create: `docs/assets/stylesheets/extra.css`
- Modify: `docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md`

**Interfaces:**
- Consumes: Material DOM classes and fenced `.mermaid` blocks.
- Produces: accessible light/dark callouts, overflow-safe tables/code/diagrams, print rules, and diagrams rendered by Material's native integration.

- [ ] **Step 1: Verify presentation tests fail**

Run: `python -m unittest tests.test_site.PresentationTests -v`

Expected: missing CSS and missing semantic callout markers.

- [ ] **Step 2: Implement the visual tokens and responsive behavior**

Add named CSS variables, homepage thesis and route rail, restrained cards, semantic admonitions, 74-character reading width, mobile overflow containers, visible keyboard focus, reduced-motion handling, and print overrides.

- [ ] **Step 3: Add Mermaid handling and course diagrams**

Use Material for MkDocs 9.7.7's native Mermaid initialization, which supports instant navigation and light/dark schemes. Preserve the three supplied diagrams and add small verified diagrams only where they directly clarify Region/Zone, route selection, firewall evaluation, and IP reachability.

- [ ] **Step 4: Run presentation tests**

Run: `python -m unittest tests.test_site.PresentationTests -v`

Expected: all presentation tests pass.

### Task 4: Template, documentation, and secure deployment

**Files:**
- Create: `templates/course-note-template.md`
- Create: `README.md`
- Create: `.github/workflows/deploy-pages.yml`

**Interfaces:**
- Consumes: `requirements.txt`, `mkdocs.yml`, and the validated `site/` build.
- Produces: a reusable authoring flow and Pages deployment from an uploaded artifact.

- [ ] **Step 1: Verify workflow/documentation tests fail**

Run: `python -m unittest tests.test_site.ProjectOperationsTests -v`

Expected: missing workflow, template, and operating instructions.

- [ ] **Step 2: Add the flexible course template**

Provide front matter, one H1, optional chapter sections, semantic admonition examples, Bash/text separation, official-source links, and an explicit final-update field outside `docs/`.

- [ ] **Step 3: Add GitHub Pages workflow**

Use `actions/checkout@v6`, `actions/setup-python@v6`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v4`, and `actions/deploy-pages@v4`; run tests and `mkdocs build --strict`; grant only `contents: read`, `pages: write`, and `id-token: write`.

- [ ] **Step 4: Add operating documentation**

Document PowerShell and WSL setup/serve/build commands, Pages source selection, repository path configuration, adding a course, custom-domain reservation, deployment diagnostics, and secret hygiene.

- [ ] **Step 5: Run operations tests**

Run: `python -m unittest tests.test_site.ProjectOperationsTests -v`

Expected: all operations tests pass.

### Task 5: Build, browser QA, Git, and publication

**Files:**
- Verify: all project files
- Generated but ignored: `site/`

**Interfaces:**
- Consumes: the entire repository.
- Produces: a tested local commit and a GitHub Pages-ready `main` branch on `dai2330/gcp-cloud-based-certification-exam-notes`.

- [ ] **Step 1: Install reproducible dependencies**

Run: `python -m pip install -r requirements.txt`

Expected: MkDocs Material 9.7.7 installs successfully.

- [ ] **Step 2: Run the complete test and build suite**

Run: `python -m unittest discover -s tests -v`

Expected: all tests pass with zero failures.

Run: `python -m mkdocs build --strict`

Expected: exit code 0 and generated `site/index.html` plus the normalized course URL.

- [ ] **Step 3: Run browser QA**

Serve with `python -m mkdocs serve --dev-addr 127.0.0.1:8000`; use Playwright at desktop and mobile widths to verify homepage/course navigation, light/dark controls, Chinese search UI, code copy controls, table/diagram overflow, and absence of browser console errors.

- [ ] **Step 4: Review repository safety and diff**

Run: `git status --short`, `git diff --check`, and a tracked-file secret-pattern scan.

Expected: no generated `site/`, credentials, trailing-whitespace errors, or unresolved placeholders.

- [ ] **Step 5: Commit and publish**

Rename the branch to `main`, commit with `feat: build GCP ACE course notes site`, authenticate GitHub CLI if needed, connect the existing private repository `dai2330/gcp-cloud-based-certification-exam-notes`, push `main`, and set Pages source to GitHub Actions.

- [ ] **Step 6: Verify remote state**

Run: `gh repo view dai2330/gcp-cloud-based-certification-exam-notes`, `gh run list --repo dai2330/gcp-cloud-based-certification-exam-notes`, and inspect the Pages workflow result.

Expected: repository is public, `main` is pushed, and the deployment workflow is queued or successful; if GitHub authentication needs user interaction, report that as the only remaining external blocker.
