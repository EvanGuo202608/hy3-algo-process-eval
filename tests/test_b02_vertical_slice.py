import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from algotrace_hy3.evaluator.aggregate import aggregate_result
from algotrace_hy3.evaluator.rules import evaluate_process_rules
from algotrace_hy3.evaluator.sandbox import collect_test_cases, compile_and_run_cpp


class B02VerticalSliceTests(unittest.TestCase):
    def _load(self, name):
        return json.loads((ROOT / "fixtures/b02_cut_height" / name).read_text())

    def test_reference_solution_passes_tests(self):
        code = (ROOT / "benchmarks/problems/B02-cut-height/reference_solution.cpp").read_text()
        cases = collect_test_cases(ROOT / "benchmarks/problems/B02-cut-height")
        result = compile_and_run_cpp(code, cases)
        self.assertEqual(result["verdict"], "AC")
        self.assertEqual(result["passed"], result["total"])

    def test_correct_answer_wrong_process_is_detected(self):
        solution = self._load("wrong_process_right_code.json")
        cases = collect_test_cases(ROOT / "benchmarks/problems/B02-cut-height")
        program = compile_and_run_cpp(solution["code"], cases)
        process = evaluate_process_rules(solution)
        result = aggregate_result(solution, program, process)
        self.assertTrue(result["final_correct"])
        self.assertFalse(result["process_correct"])
        self.assertEqual(result["first_error_step"], 1)
        self.assertTrue(result["correct_answer_wrong_process"])

    def test_int_overflow_bug_fails_tests(self):
        solution = self._load("wrong_code_int_overflow.json")
        cases = collect_test_cases(ROOT / "benchmarks/problems/B02-cut-height")
        program = compile_and_run_cpp(solution["code"], cases)
        self.assertNotEqual(program["verdict"], "AC")


if __name__ == "__main__":
    unittest.main()
