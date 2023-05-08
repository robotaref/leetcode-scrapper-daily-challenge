import json
import unittest
from typing import List


class TestCase:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        return f"inputs: {self.inputs}, output: {self.outputs}"


class BaseSolutionTest(unittest.TestCase):
    config_file = str
    solution_class = None
    example_files: str = None

    def __init__(self, solution_class, example_files="test_cases.json", used_tests=None):
        super().__init__()
        self.used_tests = used_tests
        self.solution_class = solution_class
        self.test_cases = self.read_test_cases(example_files)
        self.test_examples()

    def test_examples(self):
        for i,test_case in enumerate(self.test_cases):
            if self.used_tests is None or i in self.used_tests:
                self.assert_test_case(test_case)

    def assert_test_case(self, test_case):
        print(test_case)
        try:
            self.assertEqual(self.solution_class.main(**test_case.inputs), test_case.outputs)
            print("ok")
        except self.failureException as e:
            print(repr(e))

    @staticmethod
    def read_test_cases(example_files: str) -> List[TestCase]:
        f = open(example_files)
        data = json.load(f)
        test_cases: List[TestCase] = []
        for name, test_case in data.items():
            test_cases.append(TestCase(name, test_case['input'], test_case['output']))
        return test_cases
