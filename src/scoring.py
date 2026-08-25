"""Transparent opportunity scoring for the Legal AI Transformation Hub."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


WEIGHTS = {
    "business_impact": 0.20,
    "hours_saved_potential": 0.15,
    "client_value": 0.15,
    "strategic_alignment": 0.15,
    "feasibility": 0.15,
    "adoption_readiness": 0.10,
    "effort": -0.05,
    "risk": -0.05,
}


def _validate_rating(name: str, value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number from 1 to 5")
    if not 1 <= value <= 5:
        raise ValueError(f"{name} must be between 1 and 5")
    return float(value)


def calculate_priority(data: dict[str, Any]) -> dict[str, Any]:
    """Return an explainable 0-100 score and recommended priority band."""
    missing = [key for key in WEIGHTS if key not in data]
    if missing:
        raise ValueError(f"Missing scoring fields: {', '.join(missing)}")

    components: dict[str, float] = {}
    weighted_total = 0.0
    for field, weight in WEIGHTS.items():
        rating = _validate_rating(field, data[field])
        contribution = rating * weight
        components[field] = round(contribution * 20, 2)
        weighted_total += contribution

    # Maximum theoretical positive score is 3.75 and minimum penalty is -0.50.
    # Normalization keeps the result intuitive while preserving ranking.
    raw_score = weighted_total * 20
    normalized_score = round(max(0.0, min(100.0, raw_score + 10.0)), 2)

    risk = float(data["risk"])
    feasibility = float(data["feasibility"])
    if risk >= 5:
        band = "Governance Review Required"
    elif feasibility <= 2:
        band = "Discovery Required"
    elif normalized_score >= 75 and float(data["effort"]) <= 3:
        band = "Quick Win"
    elif normalized_score >= 65:
        band = "Strategic Initiative"
    elif normalized_score >= 50:
        band = "Discovery Required"
    else:
        band = "Defer"

    return {
        "priority_score": normalized_score,
        "priority_band": band,
        "components": components,
        "formula_version": "1.0.0",
    }


def estimate_annual_benefit(data: dict[str, Any]) -> dict[str, float]:
    required = ("monthly_volume", "minutes_per_transaction", "automation_rate")
    missing = [field for field in required if field not in data]
    if missing:
        raise ValueError(f"Missing benefit fields: {', '.join(missing)}")

    volume = float(data["monthly_volume"])
    minutes = float(data["minutes_per_transaction"])
    automation_rate = float(data["automation_rate"])
    if volume < 0 or minutes < 0 or not 0 <= automation_rate <= 1:
        raise ValueError("Benefit inputs must be non-negative and automation_rate 0-1")

    hours = volume * 12 * minutes * automation_rate / 60
    rate = float(data.get("loaded_hourly_rate", 0))
    return {
        "expected_annual_hours_saved": round(hours, 2),
        "expected_annual_value": round(hours * rate, 2),
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python src/scoring.py <opportunity.json>")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    output = {
        "opportunity": data.get("title", "Untitled"),
        **calculate_priority(data["scoring"]),
        **estimate_annual_benefit(data["benefit_assumptions"]),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

