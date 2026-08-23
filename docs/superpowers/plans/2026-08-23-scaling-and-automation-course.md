# Scaling and Automation Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Elastic Google Cloud Infrastructure: Scaling and Automation as the third ACE single-page course and publish it with the current GitHub Pages workflow.

**Architecture:** Reuse the current MkDocs Material content model while introducing a separate Elastic Google Cloud Infrastructure navigation series. Import the supplied Markdown with heading-only normalization and expose it through the global navigation, homepage, and ACE learning path.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown file maps to one generated webpage.
- Preserve every non-heading source line in original order.
- Use the path `certification / course series / course page`.
- Do not modify the existing visual or deployment architecture.

---

### Task 1: Add acceptance coverage

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Elastic_Google_Cloud_Infrastructure_Scaling_and_Automation.source.txt`

**Interfaces:**
- Consumes: the supplied 821-line Markdown source.
- Produces: assertions for path, heading hierarchy, source preservation, navigation order, and discovery links.

- [ ] Add the source fixture and tests for a unique H1, five Chapter H2 headings, ordered preservation of all non-heading lines, and links from `mkdocs.yml`, the homepage, and the ACE learning path.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm the new tests fail because the course page and links do not exist.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/elastic-google-cloud-infrastructure/elastic-google-cloud-infrastructure-scaling-and-automation.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 acceptance requirements.
- Produces: one generated course page in a distinct Elastic Google Cloud Infrastructure series.

- [ ] Keep the course title as H1; convert Chapter and summary H1 headings to H2; move nested H2/H3 headings down one level after the first Chapter.
- [ ] Add the new series after Essential Google Cloud Infrastructure and add the course to all discovery surfaces.
- [ ] Run the full unit test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after content verification.

**Interfaces:**
- Consumes: the verified site from Task 2.
- Produces: a public GitHub Pages course URL based on the new `main` commit.

- [ ] Run the full test suite, `.\.venv\Scripts\mkdocs.exe build --strict`, `git diff --check`, static artifact checks, and a secret-pattern scan.
- [ ] Commit with `feat: add Scaling and Automation course notes` and push `main`.
- [ ] Wait for the Pages workflow and verify the public page returns HTTP 200 with the expected title and chapter markers.
