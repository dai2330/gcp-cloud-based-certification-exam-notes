# AI Infrastructure Cloud TPUs Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish AI Infrastructure: Cloud TPUs as the ninth ACE single-page course.

**Architecture:** Add a second page to the existing AI Infrastructure course-series directory and reuse the current MkDocs presentation. Normalize headings only outside fenced code blocks so shell comments remain source content.

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
- Create: `tests/fixtures/ACE_AI_Infrastructure_Cloud_TPUs.source.txt`

**Interfaces:**
- Consumes: the 585-line UTF-8 supplied source.
- Produces: tests for path, heading hierarchy, code comments, preservation, diagrams, ordering, and discovery links.

- [ ] Add the fixture and four course tests.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm failure is caused by the missing page and links.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/ai-infrastructure/ai-infrastructure-cloud-tpus.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements.
- Produces: one Cloud TPUs page reachable from all discovery surfaces after Cloud GPUs.

- [ ] Transform only headings outside fenced code and preserve every code comment.
- [ ] Add the Cloud TPUs child entry, ninth homepage rail/card, and ninth learning-path course.
- [ ] Run the full test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, strict build, whitespace check, artifact assertions, and secret scan.
- [ ] Commit with `feat: add AI Infrastructure Cloud TPUs course notes` and push `main`.
- [ ] Wait for Pages and verify HTTP 200 plus the title and core chapter markers.
