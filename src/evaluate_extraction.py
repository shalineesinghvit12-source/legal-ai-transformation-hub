"""Evaluate structured AI extraction against a synthetic expected result."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def normalize(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "|".join(sorted(normalize(item) for item in value))
    return " ".join(str(value).lower().split())


def evaluate(expected: dict[str, Any], actual: dict[str, Any]) -> dict[str, Any]:
    fields = sorted(expected)
    results = []
    matches = 0
    for field in fields:
        expected_value = expected[field]
        actual_value = actual.get(field)
        matched = normalize(expected_value) == normalize(actual_value)
        matches += int(matched)
        results.append(
            {
                "field": field,
                "matched": matched,
                "expected": expected_value,
                "actual": actual_value,
            }
        )
    accuracy = round(matches / len(fields), 4) if fields else 0.0
    return {"field_accuracy": accuracy, "matched": matches, "total": len(fields), "details": results}


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python src/evaluate_extraction.py expected.json actual.json")
    expected = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    actual = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(expected, actual), indent=2))


if __name__ == "__main__":
    main()

