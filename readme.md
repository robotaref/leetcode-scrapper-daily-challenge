This repo is created for daily challenges of [LeetCode](https://leetcode.com/), starting from April 1, 2023, mostly with `python3`.

_IMPORTANT NOTICE_: some codes are gathered from internet and not all of them are not my original work.

### Getting Questions

First, install requirements:

```shell
pip install -r requirements.txt -U 
```

To get any question, with problem and description, use download command.

```shell
python main.py -d True 
```

and to get any other, use:

```shell
python main.py -s `QUESTION_SLUG`
```

`QUESTION_SLUG` can be extracted from any problem url, which looks like this:

https://leetcode.com/problems/{QUESTION_SLUG}/

### Running Locally

Most questions consist of a `class Solution`, and a `mainMethod(**kwargs)` that needs to be implemented.
To be able to run this file, simply create a `python` file with this schema:

```python
from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.main = self.mainMethod

    def mainMethod(self, **kwargs):


BaseSolutionTest(Solution, )
```

To twick your tests a little, you can create `BaseSolutionTest` with optional inputs.
example_file is obvious, but to use specific tests, define them by providing a list, with relevant IDs (i.e `[1,3]`).

```python
BaseSolutionTest(self, solution_class, example_files: str = "test_cases.json", used_tests:List = None):
```

This file will be added automatically if you use download command.

You can add your own test cases, by simply adding to `{DIFFICULTY}/{QUESTION_ID}/test_cases.json`, just use the correct
schema:

```json
{
  "TEST_NAME": {
    "input": {
      "FIRST_INPUT_NAME": "VALUE"
    },
    "output": "OUTPUT_VALUE"
  }
}
```