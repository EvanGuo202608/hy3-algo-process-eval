import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from algotrace_hy3.schemas import SchemaError, validate_solution


class SchemaTests(unittest.TestCase):
    def test_correct_fixture_is_valid(self):
        data = json.loads((ROOT / "fixtures/a01_pack_cost/correct.json").read_text())
        self.assertEqual(validate_solution(data), [])

    def test_invalid_dependency_is_rejected(self):
        data = json.loads((ROOT / "fixtures/a01_pack_cost/correct.json").read_text())
        data["steps"][0]["depends_on"] = [99]
        with self.assertRaises(SchemaError):
            validate_solution(data)


if __name__ == "__main__":
    unittest.main()

