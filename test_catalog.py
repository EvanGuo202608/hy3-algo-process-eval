from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_problem_catalog import validate_catalog


class CatalogTests(unittest.TestCase):
    def test_catalog_stage1_counts(self):
        result = validate_catalog(ROOT / "benchmarks/problem_catalog.yaml")
        self.assertTrue(result["ok"])
        self.assertEqual(result["candidate_count"], 20)
        self.assertEqual(result["mvp_count"], 8)


if __name__ == "__main__":
    unittest.main()

