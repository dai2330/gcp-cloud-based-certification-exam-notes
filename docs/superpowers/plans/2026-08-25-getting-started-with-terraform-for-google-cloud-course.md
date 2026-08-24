# Getting Started with Terraform for Google Cloud Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Getting Started with Terraform for Google Cloud as the twelfth ACE single-page course.

**Architecture:** Add a new course-series directory and reuse the current MkDocs presentation. Normalize only the source page title because the supplied H2/H3 hierarchy is already valid; preserve fenced code verbatim.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown maps to one webpage.
- Preserve all non-heading source lines in order.
- Preserve the 16 numbered H2 sections and their H3 children.
- Keep all HCL, Bash, and text fences unchanged.
- Keep the current visual and deployment architecture.
- Publish directly from `main`, following the user's established repository workflow.

---

### Task 1: Add failing acceptance tests

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Getting_Started_with_Terraform_for_Google_Cloud.source.txt`

**Interfaces:**
- Consumes: the 599-line UTF-8 supplied source.
- Produces: tests for path, heading hierarchy, fenced code preservation, ordering, and discovery links.

- [ ] Add the fixture and four course tests.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm failure is caused by the missing page and links.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/getting-started-with-terraform-for-google-cloud/getting-started-with-terraform-for-google-cloud.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements.
- Produces: one Terraform page reachable from all discovery surfaces after Logging and Monitoring.

- [ ] Normalize only the H1 title and preserve all other headings and fenced code.
- [ ] Add the new series, twelfth homepage rail/card, and twelfth learning-path course.
- [ ] Run the full test suite and confirm all tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, strict build, whitespace check, artifact assertions, and secret scan.
- [ ] Commit with `feat: add Getting Started with Terraform for Google Cloud course notes` and push `main`.
- [ ] Wait for Pages and verify HTTP 200 plus the title and Terraform workflow markers.
