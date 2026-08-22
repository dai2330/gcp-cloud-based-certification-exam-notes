# Core Services Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the Core Services course as a second single-page course in the existing ACE documentation site and publish it through the current GitHub Pages workflow.

**Architecture:** Reuse the existing MkDocs Material course hierarchy and presentation. Import the supplied Markdown into the Essential Google Cloud Infrastructure course folder, normalize only heading levels, and expose the page through the existing navigation, homepage, and ACE learning path.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown file maps to one generated webpage.
- Preserve every non-heading source line in its original order.
- Keep the repository hierarchy `certification / course series / course page`.
- Do not change the current visual system or deployment architecture.

---

### Task 1: Add Core Services acceptance coverage

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Essential_Google_Cloud_Infrastructure_Core_Services.source.txt`

**Interfaces:**
- Consumes: the supplied Core Services Markdown and current site paths.
- Produces: assertions for the destination path, title hierarchy, source preservation, navigation, and discovery links.

- [ ] Add constants for the Core Services source fixture and destination page, plus tests that require a unique H1, five Chapter H2 headings, ordered preservation of non-heading source lines, and links in all discovery surfaces.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and verify the new tests fail because the course page and links do not exist.

### Task 2: Import the course and update discovery surfaces

**Files:**
- Create: `docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-core-services.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: the acceptance requirements from Task 1.
- Produces: one MkDocs course page reachable from navigation, homepage, and ACE learning path.

- [ ] Transform source headings so the course title is the only H1, Chapter and summary headings are H2, and nested headings retain their relative hierarchy.
- [ ] Add Core Services immediately after Foundation in navigation and course discovery content.
- [ ] Run the full unit test suite and confirm all tests pass.

### Task 3: Verify, publish, and check the deployed page

**Files:**
- Modify: Git history only; no additional production files expected.

**Interfaces:**
- Consumes: the verified site from Task 2.
- Produces: a published `main` commit and an HTTP-accessible Core Services page.

- [ ] Run `.\.venv\Scripts\mkdocs.exe build --strict`, `git diff --check`, and the full unit test suite.
- [ ] Commit with `feat: add Core Services course notes` and push `main` to `origin`.
- [ ] Wait for the Pages workflow to conclude successfully.
- [ ] Request the deployed Core Services URL and verify HTTP 200 plus the expected course title.
