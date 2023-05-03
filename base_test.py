import json
import unittest
from typing import List


class TestCase:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs


class BaseSolutionTest(unittest.TestCase):
    config_file = str
    solution_class = None
    example_files: str = None

    def __init__(self, solution_class, example_files="test_cases.json"):
        super().__init__()
        self.solution_class = solution_class
        self.test_cases = self.read_test_cases(example_files)
        self.test_examples()

    def test_examples(self):
        for test_case in self.test_cases:
            self.assert_test_case(test_case)

    def assert_test_case(self, test_case):
        self.assertEqual(self.solution_class.main(**test_case.inputs), test_case.outputs)

    @staticmethod
    def read_test_cases(example_files: str) -> List[TestCase]:
        f = open(example_files)
        data = json.load(f)
        test_cases: List[TestCase] = []
        for _, test_case in data.items():
            test_cases.append(TestCase(test_case['input'], test_case['output']))
        return test_cases
