# Deploy Kubernetes Applications on Google Cloud Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Deploy Kubernetes Applications on Google Cloud as the fourteenth ACE single-page course.

**Architecture:** Add a new course-series directory and reuse the current MkDocs presentation. Normalize headings only outside fenced code blocks so Dockerfile, YAML, Bash, text, and Mermaid content remains verbatim.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown maps to one webpage.
- Preserve all non-heading source lines in order.
- Keep all fenced code unchanged.
- Keep the current visual and deployment architecture.
- Publish directly from `main`, following the user's established repository workflow.

---

### Task 1: Add failing acceptance tests

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Deploy_Kubernetes_Applications_on_Google_Cloud.source.txt`

**Interfaces:**
- Consumes: the 862-line UTF-8 supplied source.
- Produces: tests for path, heading hierarchy, fenced code, diagrams, preservation, ordering, and discovery links.

- [ ] Add the fixture and four course tests.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm failure is caused by the missing page and links.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/deploy-kubernetes-applications-on-google-cloud/deploy-kubernetes-applications-on-google-cloud.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements.
- Produces: one Kubernetes applications page reachable from all discovery surfaces after GSP313.

- [ ] Normalize headings outside fenced code and preserve all supplied code examples.
- [ ] Add the new series, fourteenth homepage rail/card, and fourteenth learning-path course.
- [ ] Run the full test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, strict build, whitespace check, artifact assertions, and secret scan.
- [ ] Commit with `feat: add Deploy Kubernetes Applications course notes` and push `main`.
- [ ] Wait for Pages and verify HTTP 200 plus Artifact Registry, GKE, and GSP318 markers.
