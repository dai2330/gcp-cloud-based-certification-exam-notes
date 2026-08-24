# Build Infrastructure with Terraform on Google Cloud Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish Build Infrastructure with Terraform on Google Cloud as an ACE single-page course positioned directly after Getting Started with Terraform for Google Cloud.

**Architecture:** Add a dedicated course directory while preserving the existing Getting Started public URL. Group both courses under a Terraform on Google Cloud navigation series and normalize headings only outside fenced code blocks so Bash, HCL, text, and Mermaid content remains verbatim.

**Tech Stack:** Markdown, MkDocs 1.6.1, Material for MkDocs 9.7.7, Python `unittest`, GitHub Actions, GitHub Pages.

## Global Constraints

- One course Markdown maps to one webpage.
- Preserve all non-heading source lines in order.
- Keep all fenced code unchanged.
- Keep the current visual and deployment architecture.
- Preserve the existing Getting Started course URL.
- Publish directly from `main`, following the user's established repository workflow.

---

### Task 1: Add failing acceptance tests

**Files:**
- Modify: `tests/test_site.py`
- Create: `tests/fixtures/ACE_Build_Infrastructure_with_Terraform_on_Google_Cloud.source.txt`

**Interfaces:**
- Consumes: the 940-line UTF-8 supplied source.
- Produces: tests for path, heading hierarchy, fenced code, diagram count, source preservation, Terraform-series ordering, and discovery links.

- [ ] Add the 940-line source fixture with Markdown hard breaks normalized to `<br>`, plus four `BuildInfrastructureTerraformCourseTests` cases.
- [ ] Assert one page H1, seven Chapter H2 headings, the certification summary, 1 Mermaid, 13 Bash, 11 HCL, and 13 text fences.
- [ ] Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` and confirm the four new tests fail because the page and discovery links do not exist.

### Task 2: Import and expose the course

**Files:**
- Create: `docs/courses/ace/build-infrastructure-with-terraform-on-google-cloud/build-infrastructure-with-terraform-on-google-cloud.md`
- Modify: `mkdocs.yml`
- Modify: `docs/index.md`
- Modify: `docs/ace/learning-path.md`

**Interfaces:**
- Consumes: Task 1 requirements and the existing Getting Started course path.
- Produces: one Terraform infrastructure page reachable from all discovery surfaces immediately after Getting Started.

- [ ] Normalize headings outside fenced code, trim fenced-code trailing whitespace only, and convert Markdown hard breaks outside fences to `<br>`.
- [ ] Replace the standalone Getting Started navigation node with a `Terraform on Google Cloud` series containing both course pages without changing the old URL.
- [ ] Add the homepage rail/card after Getting Started and insert learning-path item 13 while renumbering the following two items.
- [ ] Run the full test suite and confirm all 70 tests pass.

### Task 3: Verify and publish

**Files:**
- Modify: Git history only after verification.

**Interfaces:**
- Consumes: verified MkDocs sources.
- Produces: a deployed public course URL based on the new `main` commit.

- [ ] Run all tests, `.\.venv\Scripts\mkdocs.exe build --strict`, `git diff --check`, rendered artifact assertions, and the repository secret scan.
- [ ] Stage exactly the fixture, course, three discovery files, tests, specification, and plan.
- [ ] Repeat the tests, strict build, and cached diff check after staging.
- [ ] Commit with `feat: add Build Infrastructure with Terraform course notes` and push `main`.
- [ ] Wait for the matching Pages workflow and verify HTTP 200 plus Terraform import, remote state, Registry module, firewall, and GSP345 markers.
