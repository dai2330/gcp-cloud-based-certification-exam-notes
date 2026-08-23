# GKE Getting Started Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Getting Started with Google Kubernetes Engine as the fourth ACE single-page course.

**Architecture:** Add a Google Kubernetes Engine course-series directory and reuse the current MkDocs presentation. Normalize headings only outside fenced code blocks so shell comments remain executable example content.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown maps to one webpage.
- Preserve all non-heading source lines in order.
- Never reinterpret `#` lines inside fenced code as Markdown headings.
- Keep the current design and deployment workflow.

---

### Task 1: Add failing acceptance tests

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Getting_Started_with_Google_Kubernetes_Engine.source.txt`

**Interfaces:**
- Consumes: the 392-line supplied source.
- Produces: tests for page path, external-fence headings, code comments, content preservation, diagrams, and discovery links.

- [ ] Add the fixture and four course tests.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm failure is caused by the missing page and links.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/google-kubernetes-engine/getting-started-with-google-kubernetes-engine.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements.
- Produces: one GKE course page reachable from all discovery surfaces.

- [ ] Transform only headings outside code fences and preserve Bash comment lines verbatim.
- [ ] Add the Google Kubernetes Engine series and the fourth course entry.
- [ ] Run the full test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, strict build, whitespace check, artifact assertions, and secret scan.
- [ ] Commit with `feat: add GKE Getting Started course notes` and push `main`.
- [ ] Wait for Pages and verify HTTP 200 plus the title and Kubernetes chapter markers.
