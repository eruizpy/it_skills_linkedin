"""Pruebas de contrato; todos los perfiles y archivos son sintéticos.

Por defecto se importa skills/linkedin-profile-optimizer/scripts/check_profile.py.
LINKEDIN_CHECK_PROFILE_SCRIPT permite comprobar una ubicación canónica antes
de copiar la skill al proyecto. Ejecutar con PYTHONDONTWRITEBYTECODE=1.
"""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = Path(os.environ.get(
    "LINKEDIN_CHECK_PROFILE_SCRIPT",
    str(PROJECT_ROOT / "skills" / "linkedin-profile-optimizer" / "scripts" /
        "check_profile.py"),
)).resolve()
spec = importlib.util.spec_from_file_location("linkedin_profile_checker", SCRIPT_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("No se pudo cargar el comprobador de perfiles.")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def valid_profile():
    return {"es": {"headline": "QA", "about": "OK"},
            "en": {"headline": "QA", "about": "OK"}}


def codes(report):
    return {issue["code"] for issue in report["issues"]}


class ProfileContractTests(unittest.TestCase):
    def test_exact_unicode_code_points_without_normalization_or_trimming(self):
        for value, expected in [("é", 1), ("e\u0301", 2), ("😀", 1),
                                ("👩\u200d💻", 3), ("🇪🇸", 2), (" a\n", 3)]:
            with self.subTest(value=repr(value)):
                profile = valid_profile()
                profile["es"]["headline"] = value
                report = checker.check_profile(profile)
                self.assertEqual(report["counts"]["es"]["headline"], expected)
                self.assertEqual(report["status"], "ok")
                self.assertEqual(report["counting_unit"], "unicode_code_points")

    def test_empty_and_whitespace_only_fields(self):
        for value, expected in [("", 0), (" \t\n", 3), ("\u00a0\u2003", 2)]:
            with self.subTest(value=repr(value)):
                profile = valid_profile()
                profile["en"]["about"] = value
                report = checker.check_profile(profile)
                self.assertIn("empty_field", codes(report))
                self.assertEqual(report["counts"]["en"]["about"], expected)

    def test_field_types_are_not_coerced(self):
        for value in (None, True, False, 42, 1.5, [], {}):
            with self.subTest(value=value):
                profile = valid_profile()
                profile["es"]["about"] = value
                report = checker.check_profile(profile)
                self.assertEqual(codes(report), {"invalid_field_type"})
                self.assertIsNone(report["counts"]["es"]["about"])
                self.assertEqual(report["status"], "needs_review")

    def test_root_languages_and_required_fields(self):
        for root in ([], None, 1, "text"):
            with self.subTest(root=root):
                self.assertEqual(codes(checker.check_profile(root)), {"invalid_root_type"})
        profile = valid_profile()
        del profile["en"]
        self.assertIn("missing_language", codes(checker.check_profile(profile)))
        for value in (None, [], "text", True):
            with self.subTest(language_type=value):
                profile = valid_profile()
                profile["es"] = value
                self.assertIn("invalid_language_type", codes(checker.check_profile(profile)))
        for language in ("es", "en"):
            for field in ("headline", "about"):
                with self.subTest(language=language, field=field):
                    profile = valid_profile()
                    del profile[language][field]
                    report = checker.check_profile(profile)
                    self.assertEqual(codes(report), {"missing_field"})
                    self.assertIsNone(report["counts"][language][field])

    def test_default_targets_are_inclusive_for_both_languages(self):
        for language in ("es", "en"):
            for field, target in (("headline", 180), ("about", 2000)):
                for length, warns in ((target - 1, False), (target, False),
                                      (target + 1, True)):
                    with self.subTest(language=language, field=field, length=length):
                        profile = valid_profile()
                        profile[language][field] = "x" * length
                        report = checker.check_profile(profile)
                        self.assertEqual("exceeds_target" in codes(report), warns)
                        self.assertEqual(report["counts"][language][field], length)
                        self.assertEqual(report["target_kind"], "editorial")
                        self.assertIn("no límites oficiales", report["limits_note"])

    def test_custom_targets_and_invalid_api_targets(self):
        profile = valid_profile()
        profile["es"] = {"headline": "12345", "about": "1234567"}
        report = checker.check_profile(profile, headline_target=5, about_target=7)
        self.assertEqual(report["status"], "ok")
        self.assertEqual(report["targets"], {"headline": 5, "about": 7})
        for value in (0, -1, True, "5", 2.5):
            with self.subTest(target=value):
                with self.assertRaises(ValueError):
                    checker.check_profile(profile, headline_target=value)

    def test_clear_pending_markers(self):
        markers = ("[PENDIENTE]", "[TODO]", "[ todo ]", "[TODO: fecha]",
                   "[CONFIRMAR]", "[CONFIRMAR fecha]", "[CONFIRMAR...]",
                   "{{nombre}}", "{{\nnombre\n}}", "<REEMPLAZAR nombre>",
                   "<reemplazar...>", "TBD", "(tbd)")
        for value in markers:
            with self.subTest(marker=value):
                profile = valid_profile()
                profile["es"]["about"] = value
                report = checker.check_profile(profile)
                self.assertEqual(codes(report), {"pending_marker"})
                self.assertEqual(report["issues"][0]["field"], "es.about")

    def test_legitimate_words_and_marker_prefixes_are_not_flagged(self):
        for value in ("todo el ciclo de pruebas", "TODO EL CICLO", "método",
                      "TBD123", "NotTBD", "TBD_123", "[todo el ciclo]",
                      "[CONFIRMARLO]", "<REEMPLAZARLO>", "estado pendiente"):
            with self.subTest(text=value):
                profile = valid_profile()
                profile["en"]["about"] = value
                self.assertEqual(checker.check_profile(profile)["status"], "ok")

    def test_extra_fields_are_ignored_and_report_contains_no_profile_text(self):
        profile = valid_profile()
        profile["es"]["headline"] = "PRIVATE_HEADLINE_SENTINEL"
        profile["en"]["about"] = "PRIVATE_ABOUT_SENTINEL"
        profile["_note"] = "[TODO] PRIVATE_NOTE_SENTINEL"
        profile["PRIVATE_EXTRA_KEY"] = {"other": "{{PRIVATE_EXTRA_VALUE}}"}
        profile["es"]["other"] = "<REEMPLAZAR PRIVATE_OTHER_VALUE>"
        report = checker.check_profile(profile)
        serialized = json.dumps(report)
        self.assertEqual(report["status"], "ok")
        self.assertNotIn("PRIVATE_", serialized)
        self.assertEqual(report["scope"],
                         ["es.headline", "es.about", "en.headline", "en.about"])
        self.assertEqual(report["extra_fields"], "ignored")
        self.assertIn("SOLO headline/about", report["scope_note"])


class CommandLineContractTests(unittest.TestCase):
    def run_cli(self, arguments):
        # Match the pipe decoder on Windows as well as UTF-8 locales.
        environment = dict(os.environ, PYTHONIOENCODING="utf-8")
        return subprocess.run([sys.executable, "-B", str(SCRIPT_PATH), *arguments],
                              text=True, encoding="utf-8", capture_output=True,
                              check=False, timeout=10, env=environment)

    def run_document(self, document, *options):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.json"
            if isinstance(document, bytes):
                path.write_bytes(document)
            else:
                path.write_text(document, encoding="utf-8")
            return self.run_cli([str(path), *options])

    def assert_report(self, process, expected_exit):
        self.assertEqual(process.returncode, expected_exit, process.stderr)
        self.assertEqual(process.stderr, "")
        report = json.loads(process.stdout)
        self.assertIn("counts", report)
        self.assertIn("targets", report)
        self.assertIn("issues", report)
        self.assertIn("limits_note", report)
        self.assertNotIn("Traceback", process.stdout)
        return report

    def test_cli_success_custom_targets_and_warning_exit(self):
        data = json.dumps(valid_profile())
        report = self.assert_report(self.run_document(
            data, "--headline-target", "2", "--about-target", "2"), 0)
        self.assertEqual(report["targets"], {"headline": 2, "about": 2})
        self.assertEqual(report["status"], "ok")
        report = self.assert_report(self.run_document(data, "--headline-target", "1"), 1)
        self.assertIn("exceeds_target", codes(report))
        report = self.assert_report(self.run_document('{"es": {}, "en": {}}'), 1)
        self.assertIn("missing_field", codes(report))

    def test_duplicate_keys_rejected_at_every_depth_including_escaped_keys(self):
        documents = (
            '{"es": {}, "es": {}, "en": {}}',
            '{"es": {"headline": "QA", "headline": "Dev", "about": "OK"},'
            ' "en": {"headline": "QA", "about": "OK"}}',
            '{"es": {"headline": "QA", "about": "OK"},'
            ' "en": {"headline": "QA", "about": "OK"},'
            ' "extra": {"PRIVATE_DUPLICATE_KEY": 1, "PRIVATE_DUPLICATE_KEY": 2}}',
            '{"es": {}, "\\u0065s": {}}',
        )
        for document in documents:
            with self.subTest(document=document):
                process = self.run_document(document)
                report = self.assert_report(process, 2)
                self.assertEqual(codes(report), {"duplicate_key"})
                self.assertNotIn("PRIVATE_", process.stdout + process.stderr)

    def test_invalid_json_and_nonstandard_constants(self):
        for document in ('{"es":', json.dumps(valid_profile()) + ' trailing',
                         '{"extra": NaN}', '{"extra": Infinity}',
                         '{"extra": -Infinity}'):
            with self.subTest(document=document):
                report = self.assert_report(self.run_document(document), 2)
                self.assertEqual(codes(report), {"invalid_json"})
        report = self.assert_report(self.run_document(b'\xff'), 2)
        self.assertEqual(codes(report), {"invalid_encoding"})

    def test_integer_parser_limit_returns_json_instead_of_tracebacks(self):
        digit_limit = getattr(sys, "get_int_max_str_digits", lambda: 0)()
        if not digit_limit:
            self.skipTest("El intérprete no aplica un límite de dígitos enteros.")
        document = '{"extra":' + '9' * (digit_limit + 1) + '}'
        report = self.assert_report(self.run_document(document), 2)
        self.assertEqual(codes(report), {"json_parser_limit"})

    def test_missing_file_and_directory_are_friendly_private_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "PRIVATE_MISSING_FILENAME.json"
            for path in (missing, Path(directory)):
                with self.subTest(path_type="missing" if path == missing else "directory"):
                    process = self.run_cli([str(path)])
                    report = self.assert_report(process, 2)
                    self.assertEqual(codes(report), {"read_error"})
                    self.assertNotIn(str(path), process.stdout + process.stderr)

    def test_bad_arguments_always_return_json_and_exit_two(self):
        for option in ("--headline-target", "--about-target"):
            for value in ("0", "-1", "1.5", "PRIVATE_INVALID_ARGUMENT"):
                with self.subTest(option=option, value=value):
                    process = self.run_document(json.dumps(valid_profile()), option, value)
                    report = self.assert_report(process, 2)
                    self.assertEqual(codes(report), {"invalid_arguments"})
                    self.assertNotIn("PRIVATE_", process.stdout + process.stderr)
        for arguments in ([], ["--unknown", "PRIVATE_INVALID_ARGUMENT"],
                          ["--headline-target"]):
            with self.subTest(arguments=arguments):
                self.assertEqual(codes(self.assert_report(self.run_cli(arguments), 2)),
                                 {"invalid_arguments"})

    def test_cli_never_echoes_field_values_or_matched_marker_contents(self):
        profile = valid_profile()
        profile["es"]["headline"] = "PRIVATE_HEADLINE_SENTINEL"
        profile["en"]["about"] = "{{PRIVATE_PENDING_SENTINEL}}"
        process = self.run_document(json.dumps(profile))
        self.assert_report(process, 1)
        self.assertNotIn("PRIVATE_", process.stdout + process.stderr)

    def test_help_is_human_readable_and_successful(self):
        process = self.run_cli(["--help"])
        self.assertEqual(process.returncode, 0)
        self.assertEqual(process.stderr, "")
        self.assertIn("--headline-target", process.stdout)
        self.assertIn("editorial", process.stdout)


if __name__ == "__main__":
    unittest.main()
