# GSP313 Load Balancing Challenge Lab Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Implement Load Balancing on Compute Engine: Challenge Lab (GSP313) as the thirteenth ACE single-page course.

**Architecture:** Add a new course-series directory and reuse the current MkDocs presentation. Normalize the first H1, demote only the summary H1, and preserve all remaining headings and fenced code verbatim.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown maps to one webpage.
- Preserve all non-heading source lines in order.
- Preserve numbered sections and their H3/H4 children.
- Keep Bash, text, and Mermaid fences unchanged.
- Keep the current visual and deployment architecture.
- Publish directly from `main`, following the user's established repository workflow.

---

### Task 1: Add failing acceptance tests

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_GSP313_Implement_Load_Balancing_on_Compute_Engine_Challenge_Lab.source.txt`

**Interfaces:**
- Consumes: the 762-line UTF-8 supplied source.
- Produces: tests for path, heading hierarchy, fenced code, diagrams, preservation, ordering, and discovery links.

- [ ] Add the fixture and four course tests.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm failure is caused by the missing page and links.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/implement-load-balancing-on-compute-engine/implement-load-balancing-on-compute-engine-challenge-lab.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements.
- Produces: one GSP313 page reachable from all discovery surfaces after Terraform.

- [ ] Normalize the title, demote the summary H1, and preserve remaining headings and fenced code.
- [ ] Add the new series, thirteenth homepage rail/card, and thirteenth learning-path course.
- [ ] Run the full test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, strict build, whitespace check, artifact assertions, and secret scan.
- [ ] Commit with `feat: add GSP313 load balancing challenge lab notes` and push `main`.
- [ ] Wait for Pages and verify HTTP 200 plus GSP313 and load-balancer markers.
