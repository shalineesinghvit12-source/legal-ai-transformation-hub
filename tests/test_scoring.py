import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.scoring import calculate_priority, estimate_annual_benefit


class PriorityScoringTests(unittest.TestCase):
    def test_high_value_low_effort_is_quick_win(self):
        result = calculate_priority(
            {
                "business_impact": 5,
                "hours_saved_potential": 5,
                "client_value": 4,
                "strategic_alignment": 5,
                "feasibility": 4,
                "adoption_readiness": 4,
                "effort": 2,
                "risk": 2,
            }
        )
        self.assertEqual(result["priority_band"], "Quick Win")
        self.assertGreaterEqual(result["priority_score"], 75)

    def test_critical_risk_forces_governance_review(self):
        ratings = {field: 4 for field in (
            "business_impact", "hours_saved_potential", "client_value",
            "strategic_alignment", "feasibility", "adoption_readiness", "effort", "risk"
        )}
        ratings["risk"] = 5
        self.assertEqual(calculate_priority(ratings)["priority_band"], "Governance Review Required")

    def test_low_feasibility_requires_discovery(self):
        ratings = {field: 3 for field in (
            "business_impact", "hours_saved_potential", "client_value",
            "strategic_alignment", "feasibility", "adoption_readiness", "effort", "risk"
        )}
        ratings["feasibility"] = 2
        self.assertEqual(calculate_priority(ratings)["priority_band"], "Discovery Required")

    def test_invalid_rating_fails(self):
        ratings = {field: 3 for field in (
            "business_impact", "hours_saved_potential", "client_value",
            "strategic_alignment", "feasibility", "adoption_readiness", "effort", "risk"
        )}
        ratings["risk"] = 6
        with self.assertRaises(ValueError):
            calculate_priority(ratings)

    def test_annual_benefit(self):
        result = estimate_annual_benefit(
            {"monthly_volume": 200, "minutes_per_transaction": 30, "automation_rate": 0.6, "loaded_hourly_rate": 100}
        )
        self.assertEqual(result["expected_annual_hours_saved"], 720)
        self.assertEqual(result["expected_annual_value"], 72000)


if __name__ == "__main__":
    unittest.main()

