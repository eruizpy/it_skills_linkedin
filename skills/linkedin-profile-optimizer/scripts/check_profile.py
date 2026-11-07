#!/usr/bin/env python3
"""Revisar headline/about ES/EN de un JSON local, sin revelar su contenido.

Los objetivos son editoriales, no límites oficiales de LinkedIn. Cada cadena
se cuenta con len() sin normalizar ni recortar: puntos de código Unicode.
Salidas: 0 = sin incidencias, 1 = revisar campos, 2 = error de entrada.
--help muestra ayuda convencional; las demás salidas son informes JSON.
"""

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_HEADLINE_TARGET = 180
DEFAULT_ABOUT_TARGET = 2000
LANGUAGES = ("es", "en")
FIELDS = ("headline", "about")
LIMITS_NOTE = (
    "Los objetivos son editoriales, no límites oficiales de LinkedIn. "
    "El conteo usa puntos de código Unicode del texto exacto, incluidos "
    "espacios y saltos de línea; puede diferir del contador de la interfaz."
)
SCOPE_NOTE = (
    "Se revisan SOLO headline/about de es y en. Los campos extra se ignoran "
    "en la revisión editorial. No se verifica veracidad, equivalencia ES/EN "
    "ni empleabilidad."
)
MARKER_PATTERNS = (
    re.compile(r"\[\s*(?:PENDIENTE|TODO)(?:\s*:[^\]]*)?\s*\]", re.IGNORECASE),
    re.compile(r"\[\s*CONFIRMAR\b[^\]]*\]", re.IGNORECASE),
    re.compile(r"\{\{.*?\}\}", re.DOTALL),
    re.compile(r"<\s*REEMPLAZAR\b[^>]*>", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
)


class DuplicateKeyError(ValueError):
    """Una clave se repite dentro del mismo objeto JSON."""


class InvalidJSONConstantError(ValueError):
    """NaN e Infinity no pertenecen a JSON estándar."""


class ArgumentsError(ValueError):
    """Argumentos CLI inválidos, sin incorporar valores personales."""


class ReportArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # argparse puede incluir argumentos suministrados en su mensaje.
        # Emitir solo un mensaje fijo desde main().
        raise ArgumentsError()


def positive_integer(value):
    try:
        number = int(value)
    except (TypeError, ValueError):
        raise argparse.ArgumentTypeError("debe ser un entero positivo") from None
    if number <= 0:
        raise argparse.ArgumentTypeError("debe ser un entero positivo")
    return number


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError()
        result[key] = value
    return result


def reject_constant(value):
    raise InvalidJSONConstantError()


def new_report(headline_target=DEFAULT_HEADLINE_TARGET,
               about_target=DEFAULT_ABOUT_TARGET):
    return {
        "status": "ok",
        "counting_unit": "unicode_code_points",
        "targets": {"headline": headline_target, "about": about_target},
        "target_kind": "editorial",
        "limits_note": LIMITS_NOTE,
        "scope": [language + "." + field
                  for language in LANGUAGES for field in FIELDS],
        "scope_note": SCOPE_NOTE,
        "extra_fields": "ignored",
        "counts": {language: {field: None for field in FIELDS}
                   for language in LANGUAGES},
        "issues": [],
    }


def add_issue(report, code, field, message, severity="warning", **details):
    issue = {"code": code, "field": field,
             "severity": severity, "message": message}
    issue.update(details)
    report["issues"].append(issue)


def check_profile(profile, *, headline_target=DEFAULT_HEADLINE_TARGET,
                  about_target=DEFAULT_ABOUT_TARGET):
    """Devolver únicamente métricas e incidencias de los cuatro campos.

    La validación de vacío usa strip(), pero el conteo conserva la cadena
    original. Los campos adicionales no se inspeccionan editorialmente.
    """
    for target in (headline_target, about_target):
        if type(target) is not int or target <= 0:
            raise ValueError("Los objetivos deben ser enteros positivos.")
    report = new_report(headline_target, about_target)
    if not isinstance(profile, dict):
        add_issue(report, "invalid_root_type", "$",
                  "La raíz debe ser un objeto JSON con es y en.", "error")
    else:
        for language in LANGUAGES:
            if language not in profile:
                add_issue(report, "missing_language", language,
                          "Falta el objeto de este idioma.", "error")
                continue
            section = profile[language]
            if not isinstance(section, dict):
                add_issue(report, "invalid_language_type", language,
                          "El idioma debe contener un objeto JSON.", "error")
                continue
            for field in FIELDS:
                field_path = language + "." + field
                if field not in section:
                    add_issue(report, "missing_field", field_path,
                              "Falta este campo obligatorio.", "error")
                    continue
                value = section[field]
                if not isinstance(value, str):
                    add_issue(report, "invalid_field_type", field_path,
                              "El campo debe ser una cadena de texto.", "error")
                    continue
                count = len(value)
                report["counts"][language][field] = count
                if not value.strip():
                    add_issue(report, "empty_field", field_path,
                              "El campo no puede estar vacío ni contener "
                              "solo espacios en blanco.", "error")
                    continue
                if count > report["targets"][field]:
                    add_issue(report, "exceeds_target", field_path,
                              "El campo supera el objetivo editorial.")
                marker_count = sum(len(pattern.findall(value))
                                   for pattern in MARKER_PATTERNS)
                if marker_count:
                    add_issue(report, "pending_marker", field_path,
                              "Hay marcadores pendientes por resolver.",
                              marker_count=marker_count)
    if report["issues"]:
        report["status"] = "needs_review"
    return report


def emit(report):
    # Solo se serializan métricas y mensajes fijos; nunca valores del perfil,
    # claves extra, rutas de entrada ni mensajes originales de excepciones.
    json.dump(report, sys.stdout, ensure_ascii=True, indent=2)
    sys.stdout.write("\n")


def fail(code, message, headline_target=DEFAULT_HEADLINE_TARGET,
         about_target=DEFAULT_ABOUT_TARGET):
    report = new_report(headline_target, about_target)
    report["status"] = "error"
    add_issue(report, code, "$", message, "error")
    emit(report)
    return 2


def main(argv=None):
    parser = ReportArgumentParser(
        prog="check_profile.py", allow_abbrev=False,
        description="Revisar SOLO headline/about ES/EN de un JSON local UTF-8.",
        epilog=LIMITS_NOTE,
    )
    parser.add_argument("profile_json", help="archivo JSON local con es y en")
    parser.add_argument("--headline-target", type=positive_integer,
                        default=DEFAULT_HEADLINE_TARGET,
                        help="objetivo editorial positivo (por defecto: 180)")
    parser.add_argument("--about-target", type=positive_integer,
                        default=DEFAULT_ABOUT_TARGET,
                        help="objetivo editorial positivo (por defecto: 2000)")
    try:
        args = parser.parse_args(argv)
    except ArgumentsError:
        return fail(
            "invalid_arguments",
            "Argumentos inválidos. Indique un archivo JSON y objetivos enteros "
            "positivos mediante --headline-target y --about-target. "
            "Consulte --help para ver la sintaxis.",
        )
    targets = (args.headline_target, args.about_target)
    try:
        # utf-8-sig admite también el BOM de algunos editores sin cambiar
        # ninguno de los caracteres dentro de las cadenas JSON.
        raw = Path(args.profile_json).read_text(encoding="utf-8-sig")
    except UnicodeError:
        return fail("invalid_encoding", "El archivo debe usar UTF-8.", *targets)
    except (OSError, ValueError):
        return fail("read_error", "No se pudo leer el archivo. Compruebe que "
                    "exista, sea un archivo y tenga permiso de lectura.", *targets)
    try:
        profile = json.loads(raw, object_pairs_hook=unique_object,
                             parse_constant=reject_constant)
    except DuplicateKeyError:
        return fail("duplicate_key", "El JSON contiene claves duplicadas "
                    "dentro de un objeto. Elimine las duplicaciones.", *targets)
    except (json.JSONDecodeError, InvalidJSONConstantError):
        return fail("invalid_json", "El archivo no contiene un JSON válido.", *targets)
    except (ValueError, RecursionError):
        return fail("json_parser_limit", "El JSON supera los límites de "
                    "procesamiento de este intérprete.", *targets)
    report = check_profile(profile, headline_target=targets[0], about_target=targets[1])
    emit(report)
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
