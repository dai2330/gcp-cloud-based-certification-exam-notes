# Google Cloud Database Selection Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Select a Google Cloud Database for Your Applications as the seventh ACE single-page course.

**Architecture:** Add a new Google Cloud Databases course-series directory and reuse the current MkDocs presentation. Normalize headings only outside fenced code blocks so shell comments remain source content.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown maps to one webpage.
- Preserve all non-heading source lines in order.
- Keep `#` lines inside fenced code unchanged.
- Keep the current visual and deployment architecture.
- Publish directly from `main`, following the user's established repository workflow.

---

### Task 1: Add failing acceptance tests

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Select_a_Google_Cloud_Database_for_Your_Applications.source.txt`

**Interfaces:**
- Consumes: the 660-line UTF-8 supplied source.
- Produces: tests for path, heading hierarchy, code comments, preservation, diagrams, ordering, and discovery links.

- [ ] Add the fixture and four course tests.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm failure is caused by the missing page and links.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/google-cloud-databases/select-a-google-cloud-database-for-your-applications.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements.
- Produces: one database-selection page reachable from all discovery surfaces after the Cloud Run series.

- [ ] Transform only headings outside fenced code and preserve every code comment.
- [ ] Add the database-series child entry, seventh homepage rail/card, and seventh learning-path course.
- [ ] Run the full test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, strict build, whitespace check, artifact assertions, and secret scan.
- [ ] Commit with `feat: add Google Cloud database selection course notes` and push `main`.
- [ ] Wait for Pages and verify HTTP 200 plus the title and core chapter markers.
