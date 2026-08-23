from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md"
SOURCE_FIXTURE = ROOT / "tests/fixtures/ACE_Essential_Google_Cloud_Infrastructure_Foundation.source.txt"
CORE_SERVICES_COURSE = ROOT / "docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-core-services.md"
CORE_SERVICES_SOURCE_FIXTURE = ROOT / "tests/fixtures/ACE_Essential_Google_Cloud_Infrastructure_Core_Services.source.txt"
SCALING_AUTOMATION_COURSE = ROOT / "docs/courses/ace/elastic-google-cloud-infrastructure/elastic-google-cloud-infrastructure-scaling-and-automation.md"
SCALING_AUTOMATION_SOURCE_FIXTURE = ROOT / "tests/fixtures/ACE_Elastic_Google_Cloud_Infrastructure_Scaling_and_Automation.source.txt"
GKE_COURSE = ROOT / "docs/courses/ace/google-kubernetes-engine/getting-started-with-google-kubernetes-engine.md"
GKE_SOURCE_FIXTURE = ROOT / "tests/fixtures/ACE_Getting_Started_with_Google_Kubernetes_Engine.source.txt"
CLOUD_RUN_COURSE = ROOT / "docs/courses/ace/developing-applications-with-cloud-run/developing-applications-with-cloud-run-fundamentals.md"
CLOUD_RUN_SOURCE_FIXTURE = ROOT / "tests/fixtures/ACE_Developing_Applications_with_Cloud_Run_on_Google_Cloud_Fundamentals.source.txt"
CLOUD_RUN_FUNCTIONS_COURSE = ROOT / "docs/courses/ace/developing-applications-with-cloud-run/developing-applications-with-cloud-run-functions-on-google-cloud.md"
CLOUD_RUN_FUNCTIONS_SOURCE_FIXTURE = ROOT / "tests/fixtures/ACE_Developing_Applications_with_Cloud_Run_Functions_on_Google_Cloud.source.txt"


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

    def test_navigation_exposes_foundation_course(self) -> None:
        config = read("mkdocs.yml")
        self.assertIn("Foundation: courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md", config)


class CoreServicesCourseTests(unittest.TestCase):
    def test_core_services_uses_normalized_one_page_path(self) -> None:
        self.assertTrue(CORE_SERVICES_COURSE.is_file())

    def test_core_services_has_one_h1_and_five_chapter_h2s(self) -> None:
        content = CORE_SERVICES_COURSE.read_text(encoding="utf-8")
        h1s = re.findall(r"^# (?!#).+$", content, flags=re.MULTILINE)
        self.assertEqual(h1s, ["# Essential Google Cloud Infrastructure: Core Services"])
        chapter_h2s = re.findall(r"^## Chapter [1-5] — .+$", content, flags=re.MULTILINE)
        self.assertEqual(len(chapter_h2s), 5)

    def test_core_services_preserves_every_original_non_heading_line_in_order(self) -> None:
        source_lines = CORE_SERVICES_SOURCE_FIXTURE.read_text(encoding="utf-8").splitlines()
        course_lines = CORE_SERVICES_COURSE.read_text(encoding="utf-8").splitlines()
        def normalize_layout(line: str) -> str:
            return re.sub(r"<br>$", "", line).rstrip()

        original_content = [
            normalize_layout(line)
            for line in source_lines
            if not re.match(r"^#{1,6} ", line)
        ]
        normalized_course = [normalize_layout(line) for line in course_lines]

        self.assertEqual(len(source_lines), 577)

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

    def test_core_services_is_linked_from_all_discovery_surfaces(self) -> None:
        course_path = (
            "courses/ace/essential-google-cloud-infrastructure/"
            "essential-google-cloud-infrastructure-core-services.md"
        )
        config = read("mkdocs.yml")
        homepage = read("docs/index.md")
        learning_path = read("docs/ace/learning-path.md")

        self.assertIn(f"Core Services: {course_path}", config)
        self.assertLess(config.index("Foundation:"), config.index("Core Services:"))
        self.assertIn(course_path, homepage)
        self.assertIn(f"../{course_path}", learning_path)


class ScalingAndAutomationCourseTests(unittest.TestCase):
    def test_scaling_automation_uses_normalized_one_page_path(self) -> None:
        self.assertTrue(SCALING_AUTOMATION_COURSE.is_file())

    def test_scaling_automation_has_one_h1_five_chapters_and_diagrams(self) -> None:
        content = SCALING_AUTOMATION_COURSE.read_text(encoding="utf-8")
        h1s = re.findall(r"^# (?!#).+$", content, flags=re.MULTILINE)
        self.assertEqual(h1s, ["# Elastic Google Cloud Infrastructure: Scaling and Automation"])
        chapter_h2s = re.findall(r"^## Chapter [1-5] — .+$", content, flags=re.MULTILINE)
        self.assertEqual(len(chapter_h2s), 5)
        self.assertGreaterEqual(content.count("```mermaid"), 5)

    def test_scaling_automation_preserves_every_original_non_heading_line_in_order(self) -> None:
        source_lines = SCALING_AUTOMATION_SOURCE_FIXTURE.read_text(encoding="utf-8").splitlines()
        course_lines = SCALING_AUTOMATION_COURSE.read_text(encoding="utf-8").splitlines()

        def normalize_layout(line: str) -> str:
            return re.sub(r"<br>$", "", line).rstrip()

        original_content = [
            normalize_layout(line)
            for line in source_lines
            if not re.match(r"^#{1,6} ", line)
        ]
        normalized_course = [normalize_layout(line) for line in course_lines]

        self.assertEqual(len(source_lines), 821)

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

    def test_scaling_automation_is_linked_from_all_discovery_surfaces(self) -> None:
        course_path = (
            "courses/ace/elastic-google-cloud-infrastructure/"
            "elastic-google-cloud-infrastructure-scaling-and-automation.md"
        )
        config = read("mkdocs.yml")
        homepage = read("docs/index.md")
        learning_path = read("docs/ace/learning-path.md")

        self.assertIn("Elastic Google Cloud Infrastructure:", config)
        self.assertIn(f"Scaling and Automation: {course_path}", config)
        self.assertLess(
            config.index("Essential Google Cloud Infrastructure:"),
            config.index("Elastic Google Cloud Infrastructure:"),
        )
        self.assertIn(course_path, homepage)
        self.assertIn(f"../{course_path}", learning_path)


class GkeGettingStartedCourseTests(unittest.TestCase):
    def test_gke_uses_normalized_one_page_path(self) -> None:
        self.assertTrue(GKE_COURSE.is_file())

    def test_gke_has_one_page_h1_six_chapters_and_diagrams(self) -> None:
        content = GKE_COURSE.read_text(encoding="utf-8")
        outside_fence_lines: list[str] = []
        inside_fence = False
        for line in content.splitlines():
            if line.startswith("```"):
                inside_fence = not inside_fence
            elif not inside_fence:
                outside_fence_lines.append(line)

        h1s = [line for line in outside_fence_lines if re.match(r"^# (?!#).+$", line)]
        chapter_h2s = [line for line in outside_fence_lines if re.match(r"^## Chapter [1-6] — .+$", line)]
        self.assertEqual(h1s, ["# Getting Started with Google Kubernetes Engine"])
        self.assertEqual(len(chapter_h2s), 6)
        self.assertGreaterEqual(content.count("```mermaid"), 2)
        self.assertRegex(content, r"```bash\n# 啟用必要 API\n")

    def test_gke_preserves_every_original_non_heading_line_in_order(self) -> None:
        source_lines = GKE_SOURCE_FIXTURE.read_text(encoding="utf-8").splitlines()
        course_lines = GKE_COURSE.read_text(encoding="utf-8").splitlines()

        def normalize_layout(line: str) -> str:
            return re.sub(r"<br>$", "", line).rstrip()

        original_content: list[str] = []
        inside_fence = False
        for line in source_lines:
            if line.startswith("```"):
                inside_fence = not inside_fence
                original_content.append(normalize_layout(line))
            elif inside_fence or not re.match(r"^#{1,6} ", line):
                original_content.append(normalize_layout(line))

        normalized_course = [normalize_layout(line) for line in course_lines]
        self.assertEqual(len(source_lines), 392)

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

    def test_gke_is_linked_from_all_discovery_surfaces(self) -> None:
        course_path = "courses/ace/google-kubernetes-engine/getting-started-with-google-kubernetes-engine.md"
        config = read("mkdocs.yml")
        homepage = read("docs/index.md")
        learning_path = read("docs/ace/learning-path.md")

        self.assertIn("Google Kubernetes Engine:", config)
        self.assertIn(f"Getting Started: {course_path}", config)
        self.assertLess(config.index("Elastic Google Cloud Infrastructure:"), config.index("Google Kubernetes Engine:"))
        self.assertIn(course_path, homepage)
        self.assertIn(f"../{course_path}", learning_path)


class CloudRunFundamentalsCourseTests(unittest.TestCase):
    def test_cloud_run_uses_normalized_one_page_path(self) -> None:
        self.assertTrue(CLOUD_RUN_COURSE.is_file())

    def test_cloud_run_has_one_page_h1_five_chapters_and_diagrams(self) -> None:
        content = CLOUD_RUN_COURSE.read_text(encoding="utf-8")
        outside_fence_lines: list[str] = []
        inside_fence = False
        for line in content.splitlines():
            if line.startswith("```"):
                inside_fence = not inside_fence
            elif not inside_fence:
                outside_fence_lines.append(line)

        h1s = [line for line in outside_fence_lines if re.match(r"^# (?!#).+$", line)]
        chapter_h2s = [line for line in outside_fence_lines if re.match(r"^## Chapter [1-5] — .+$", line)]
        self.assertEqual(h1s, ["# Developing Applications with Cloud Run on Google Cloud: Fundamentals"])
        self.assertEqual(len(chapter_h2s), 5)
        self.assertGreaterEqual(content.count("```mermaid"), 4)
        self.assertRegex(content, r"```bash\n# 部署\n")

    def test_cloud_run_preserves_every_original_non_heading_line_in_order(self) -> None:
        source_lines = CLOUD_RUN_SOURCE_FIXTURE.read_text(encoding="utf-8").splitlines()
        course_lines = CLOUD_RUN_COURSE.read_text(encoding="utf-8").splitlines()

        def normalize_layout(line: str) -> str:
            return re.sub(r"<br>$", "", line).rstrip()

        original_content: list[str] = []
        inside_fence = False
        for line in source_lines:
            if line.startswith("```"):
                inside_fence = not inside_fence
                original_content.append(normalize_layout(line))
            elif inside_fence or not re.match(r"^#{1,6} ", line):
                original_content.append(normalize_layout(line))

        normalized_course = [normalize_layout(line) for line in course_lines]
        self.assertEqual(len(source_lines), 691)

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

    def test_cloud_run_is_linked_from_all_discovery_surfaces(self) -> None:
        course_path = (
            "courses/ace/developing-applications-with-cloud-run/"
            "developing-applications-with-cloud-run-fundamentals.md"
        )
        config = read("mkdocs.yml")
        homepage = read("docs/index.md")
        learning_path = read("docs/ace/learning-path.md")

        self.assertIn("Developing Applications with Cloud Run on Google Cloud:", config)
        self.assertIn(f"Fundamentals: {course_path}", config)
        self.assertLess(
            config.index("Google Kubernetes Engine:"),
            config.index("Developing Applications with Cloud Run on Google Cloud:"),
        )
        self.assertIn(course_path, homepage)
        self.assertIn(f"../{course_path}", learning_path)


class CloudRunFunctionsCourseTests(unittest.TestCase):
    def test_cloud_run_functions_uses_normalized_one_page_path(self) -> None:
        self.assertTrue(CLOUD_RUN_FUNCTIONS_COURSE.is_file())

    def test_cloud_run_functions_has_one_page_h1_seven_chapters_and_diagrams(self) -> None:
        content = CLOUD_RUN_FUNCTIONS_COURSE.read_text(encoding="utf-8")
        outside_fence_lines: list[str] = []
        inside_fence = False
        for line in content.splitlines():
            if line.startswith("```"):
                inside_fence = not inside_fence
            elif not inside_fence:
                outside_fence_lines.append(line)

        h1s = [line for line in outside_fence_lines if re.match(r"^# (?!#).+$", line)]
        chapter_h2s = [line for line in outside_fence_lines if re.match(r"^## Chapter [1-7] — .+$", line)]
        self.assertEqual(h1s, ["# Developing Applications with Cloud Run Functions on Google Cloud"])
        self.assertEqual(len(chapter_h2s), 7)
        self.assertEqual(content.count("```mermaid"), 6)
        self.assertRegex(content, r"```bash\n# 現行 Cloud Run Function Source deployment\n")

    def test_cloud_run_functions_preserves_every_original_non_heading_line_in_order(self) -> None:
        source_lines = CLOUD_RUN_FUNCTIONS_SOURCE_FIXTURE.read_text(encoding="utf-8").splitlines()
        course_lines = CLOUD_RUN_FUNCTIONS_COURSE.read_text(encoding="utf-8").splitlines()

        def normalize_layout(line: str) -> str:
            return re.sub(r"<br>$", "", line).rstrip()

        original_content: list[str] = []
        inside_fence = False
        for line in source_lines:
            if line.startswith("```"):
                inside_fence = not inside_fence
                original_content.append(normalize_layout(line))
            elif inside_fence or not re.match(r"^#{1,6} ", line):
                original_content.append(normalize_layout(line))

        normalized_course = [normalize_layout(line) for line in course_lines]
        self.assertEqual(len(source_lines), 933)

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

    def test_cloud_run_functions_is_linked_from_all_discovery_surfaces(self) -> None:
        fundamentals_path = (
            "courses/ace/developing-applications-with-cloud-run/"
            "developing-applications-with-cloud-run-fundamentals.md"
        )
        course_path = (
            "courses/ace/developing-applications-with-cloud-run/"
            "developing-applications-with-cloud-run-functions-on-google-cloud.md"
        )
        config = read("mkdocs.yml")
        homepage = read("docs/index.md")
        learning_path = read("docs/ace/learning-path.md")

        self.assertIn(f"Functions on Google Cloud: {course_path}", config)
        self.assertLess(config.index(f"Fundamentals: {fundamentals_path}"), config.index(course_path))
        self.assertIn(course_path, homepage)
        self.assertLess(homepage.index(fundamentals_path), homepage.index(course_path))
        self.assertIn(f"../{course_path}", learning_path)
        self.assertLess(learning_path.index(f"../{fundamentals_path}"), learning_path.index(f"../{course_path}"))


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
