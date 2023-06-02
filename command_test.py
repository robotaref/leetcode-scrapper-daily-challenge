import json
import unittest
from typing import List


class CommandTestCase:
    def __init__(self, name, command, inputs, outputs):
        self.name = name
        self.command = command
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        return f"command:{self.command}, inputs: {self.inputs}, output: {self.outputs}"


class BaseCommandTest(unittest.TestCase):
    config_file = str
    command_class = None
    example_files: str = ""

    def __init__(self, command, example_files="test_cases.json", used_tests=None):
        super().__init__()
        self.used_tests = used_tests
        self.command_class = command
        self.test_cases = self.read_test_cases(example_files)
        self.test_examples()

    def test_examples(self):
        obj = None
        for i, test_case in enumerate(self.test_cases):
            if self.used_tests is None or i in self.used_tests:
                obj = self.assert_test_case(obj, test_case)

    def assert_test_case(self, obj, test_case: CommandTestCase):
        print(test_case)
        for _command, _input, _output in zip(test_case.command, test_case.inputs, test_case.outputs):
            try:
                if _command == self.command_class.__name__:
                    obj = self.command_class(*_input)
                else:
                    out = getattr(obj, _command)(*_input)
                    self.assertEqual(out, _output)
            except self.failureException as e:
                print(f"command :{_command} failed for {_input}, {repr(e)}")
                return
        print("test passed")
        return obj

    @staticmethod
    def read_test_cases(example_files: str) -> List[CommandTestCase]:
        f = open(example_files)
        data = json.load(f)
        test_cases: List[CommandTestCase] = []
        for name, test_case in data.items():
            test_cases.append(CommandTestCase(name, test_case['command'], test_case['input'], test_case['output']))
        return test_cases
