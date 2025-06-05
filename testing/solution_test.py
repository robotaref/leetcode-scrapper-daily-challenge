import ast
import json
import unittest
from typing import List, Any

import numpy.testing
import pandas as pd


class SolutionTestCase:
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
    question_tags: list = []

    def __init__(self, solution_class, example_file="test_cases.json", used_tests=None):
        super().__init__()
        self.question_tags = self.read_tags()
        self.used_tests = used_tests
        self.solution_class = solution_class
        self.test_cases = self.read_test_cases(example_file)
        self.test_examples()

    def test_examples(self):
        for i, test_case in enumerate(self.test_cases):
            obj = self.solution_class()
            if self.used_tests is None or i in self.used_tests:
                self.assert_test_case(obj, test_case)

    def assert_test_case(self, obj, test_case):
        print(test_case)
        try:
            output = obj.main(**test_case.inputs)
            self.assertEqual(output, test_case.outputs)
            print("test passed")
        except self.failureException as e:
            print(repr(e))

    def read_test_cases(self, example_files: str) -> List[SolutionTestCase]:
        f = open(example_files)
        data = json.load(f)

        test_cases: List[SolutionTestCase] = []
        for name, test_case in data.items():
            if "database" in self.question_tags:
                inputs = {}
                for param, value in test_case["input"].items():
                    inputs[param] = pd.DataFrame(json.loads(value))
                output = pd.DataFrame(json.loads(test_case["output"]))
                test_cases.append(SolutionTestCase(name, inputs, output))
            else:
                test_cases.append(SolutionTestCase(name, test_case['input'], test_case['output']))
        return test_cases

    @staticmethod
    def read_tags() -> list:
        with open("readme.md", encoding="utf-8") as f:
            text = f.read()
            tags = text.splitlines()[-1]
        return ast.literal_eval(tags)


class ApproximateSolutionTest(BaseSolutionTest):
    decimal = int

    def __init__(self, solution_class, example_file="test_cases.json", used_tests=None, decimal=5):
        self.decimal = decimal
        super().__init__(solution_class, example_file, used_tests)

    def assertEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        return numpy.testing.assert_almost_equal(first, second, decimal=self.decimal, )
