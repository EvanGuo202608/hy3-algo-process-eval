import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from algotrace_hy3.evaluator.aggregate import aggregate_result
from algotrace_hy3.evaluator.rules import evaluate_process_rules
from algotrace_hy3.evaluator.sandbox import collect_test_cases, compile_and_run_cpp


class A01VerticalSliceTests(unittest.TestCase):
    def _load(self, name):
        return json.loads((ROOT / "fixtures/a01_pack_cost" / name).read_text())

    def test_reference_solution_passes_tests(self):
        code = (ROOT / "benchmarks/problems/A01-pack-cost/reference_solution.cpp").read_text()
        cases = collect_test_cases(ROOT / "benchmarks/problems/A01-pack-cost")
        result = compile_and_run_cpp(code, cases)
        self.assertEqual(result["verdict"], "AC")
        self.assertEqual(result["passed"], result["total"])

    def test_correct_answer_wrong_process_is_detected(self):
        solution = self._load("wrong_process_right_code.json")
        cases = collect_test_cases(ROOT / "benchmarks/problems/A01-pack-cost")
        program = compile_and_run_cpp(solution["code"], cases)
        process = evaluate_process_rules(solution)
        result = aggregate_result(solution, program, process)
        self.assertTrue(result["final_correct"])
        self.assertFalse(result["process_correct"])
        self.assertEqual(result["first_error_step"], 1)
        self.assertTrue(result["correct_answer_wrong_process"])

    def test_floor_code_fails_tests(self):
        solution = self._load("wrong_code_floor.json")
        cases = collect_test_cases(ROOT / "benchmarks/problems/A01-pack-cost")
        program = compile_and_run_cpp(solution["code"], cases)
        self.assertNotEqual(program["verdict"], "AC")


if __name__ == "__main__":
    unittest.main()

