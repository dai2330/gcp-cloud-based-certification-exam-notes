from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md"
SOURCE_FIXTURE = ROOT / "tests/fixtures/ACE_Essential_Google_Cloud_Infrastructure_Foundation.source.txt"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class ConfigurationTests(unittest.TestCase):
    def test_required_project_files_exist(self) -> None:
        for relative in (
            "mkdocs.yml",
            "requirements.txt",
            ".gitignore",
            "docs/index.md",
            "docs/ace/learning-path.md",
        ):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_mkdocs_enables_material_reading_features(self) -> None:
        config = read("mkdocs.yml")
        for marker in (
            "name: material",
            "language: zh-TW",
            "navigation.top",
            "search.highlight",
            "content.code.copy",
            "pymdownx.superfences",
            "format: !!python/name:pymdownx.superfences.fence_code_format",
            "assets/stylesheets/extra.css",
            "exclude_docs:",
            "superpowers/",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, config)

    def test_dependency_is_pinned(self) -> None:
        self.assertEqual(read("requirements.txt").strip(), "mkdocs-material==9.7.7")


class CourseContentTests(unittest.TestCase):
    def test_course_uses_normalized_one_page_path(self) -> None:
        self.assertTrue(COURSE.is_file())

    def test_course_has_exactly_one_h1_and_four_chapter_h2s(self) -> None:
        content = COURSE.read_text(encoding="utf-8")
        h1s = re.findall(r"^# (?!#).+$", content, flags=re.MULTILINE)
        self.assertEqual(h1s, ["# Essential Google Cloud Infrastructure: Foundation"])
        for chapter in range(1, 5):
            self.assertRegex(content, rf"(?m)^## Chapter {chapter} — ")

    def test_course_preserves_key_supplied_content(self) -> None:
        content = COURSE.read_text(encoding="utf-8")
        for marker in (
            "Interacting with Google Cloud",
            "Virtual Networks",
            "Virtual Machines",
            "gcloud compute networks create NETWORK_NAME",
            "認證重點統整",
            "技術核對日期：2026-08-22",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_course_preserves_every_original_non_heading_line_in_order(self) -> None:
        source_lines = SOURCE_FIXTURE.read_text(encoding="utf-8").splitlines()
        course_lines = COURSE.read_text(encoding="utf-8").splitlines()

        def normalize_layout(line: str) -> str:
            return re.sub(r"<br>$", "", line).rstrip()

        original_content = [
            normalize_layout(line)
            for line in source_lines
            if not re.match(r"^#{1,6} ", line)
        ]
        normalized_course = [normalize_layout(line) for line in course_lines]

        self.assertEqual(len(source_lines), 842)

        course_position = 0
        for source_position, source_line in enumerate(original_content, start=1):
            while course_position < len(normalized_course) and normalized_course[course_position] != source_line:
                course_position += 1
            self.assertLess(
                course_position,
                len(normalized_course),
                f"Original non-heading line {source_position} was removed: {source_line!r}",
            )
            course_position += 1

    def test_navigation_exposes_only_available_course(self) -> None:
        config = read("mkdocs.yml")
        self.assertIn("Foundation: courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md", config)
        self.assertNotIn("Core Services:", config)


class PresentationTests(unittest.TestCase):
    def test_custom_assets_cover_mobile_print_focus_and_mermaid(self) -> None:
        css = read("docs/assets/stylesheets/extra.css")
        for marker in (
            "--gcp-cloud-blue",
            ".learning-path",
            ".mermaid",
            "overflow-x: auto",
            ":focus-visible",
            "prefers-reduced-motion",
            "@media print",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, css)

        config = read("mkdocs.yml")
        self.assertNotIn("unpkg.com/mermaid", config)
        self.assertNotIn("assets/javascripts/mermaid.js", config)

    def test_course_has_diagrams_and_semantic_callouts(self) -> None:
        content = COURSE.read_text(encoding="utf-8")
        self.assertGreaterEqual(content.count("```mermaid"), 3)
        for marker in ('!!! ace "ACE 考點"', '!!! update "官方文件更新"'):
            self.assertIn(marker, content)

    def test_commands_do_not_fabricate_missing_outputs(self) -> None:
        content = COURSE.read_text(encoding="utf-8")
        self.assertIn("```bash", content)
        self.assertIn("未提供", content)
        self.assertRegex(content, r"未提供[^\n]*(?:不製造|不建立|不虛構)")


class ProjectOperationsTests(unittest.TestCase):
    def test_template_is_not_published_and_contains_optional_sections(self) -> None:
        template = read("templates/course-note-template.md")
        self.assertFalse((ROOT / "docs/templates/course-note-template.md").exists())
        for marker in (
            "# 課程完整名稱",
            "## Chapter 1 — 章節名稱",
            "### ACE 考試重點",
            "### Terminal Output",
            "## 官方來源",
            "## 最後更新",
        ):
            self.assertIn(marker, template)

    def test_pages_workflow_builds_tests_and_deploys_artifact(self) -> None:
        workflow = read(".github/workflows/deploy-pages.yml")
        for marker in (
            "branches: [main]",
            "contents: read",
            "pages: write",
            "id-token: write",
            "actions/checkout@v6",
            "actions/setup-python@v6",
            "python -m unittest discover -s tests -v",
            "python -m mkdocs build --strict",
            "actions/configure-pages@v5",
            "actions/upload-pages-artifact@v4",
            "actions/deploy-pages@v4",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, workflow)

    def test_readme_documents_local_and_github_workflows(self) -> None:
        readme = read("README.md")
        for marker in (
            "PowerShell",
            "WSL",
            "python -m mkdocs serve",
            "python -m mkdocs build --strict",
            "GitHub Pages",
            "新增下一篇課程筆記",
            "常見錯誤排查",
            "敏感資料",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, readme)


if __name__ == "__main__":
    unittest.main()
