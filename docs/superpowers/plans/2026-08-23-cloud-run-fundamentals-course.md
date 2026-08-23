# Cloud Run Fundamentals Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Developing Applications with Cloud Run on Google Cloud: Fundamentals as the fifth ACE single-page course.

**Architecture:** Add a Cloud Run course-series directory and reuse the current MkDocs presentation. Normalize headings only outside fenced code blocks so deployment comments remain code content.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown maps to one webpage.
- Preserve all non-heading source lines in order.
- Keep `#` lines inside fenced code unchanged.
- Keep the current visual and deployment architecture.

---

### Task 1: Add failing acceptance tests

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Developing_Applications_with_Cloud_Run_on_Google_Cloud_Fundamentals.source.txt`

**Interfaces:**
- Consumes: the 691-line supplied source.
- Produces: tests for path, heading hierarchy, code comments, preservation, diagrams, and discovery links.

- [ ] Add the fixture and four course tests.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm failure is caused by the missing page and links.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/developing-applications-with-cloud-run/developing-applications-with-cloud-run-fundamentals.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements.
- Produces: one Cloud Run Fundamentals page reachable from all discovery surfaces.

- [ ] Transform only headings outside fenced code and preserve deployment comments.
- [ ] Add the Cloud Run series and fifth course entry.
- [ ] Run the full test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, strict build, whitespace check, artifact assertions, and secret scan.
- [ ] Commit with `feat: add Cloud Run Fundamentals course notes` and push `main`.
- [ ] Wait for Pages and verify HTTP 200 plus the title and core chapter markers.
