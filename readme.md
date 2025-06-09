🐍 [LeetCode](https://leetcode.com/) Scraper & Local Debug Tool
Easily fetch LeetCode problems for offline practice, local testing, and building your personal solution bank.

🚀 Project Overview
This project provides a simple Python-based toolset to scrape LeetCode problems and make them available offline. It helps LeetCoders and competitive programmers streamline their workflow:

✨ Fetch the Daily Challenge problem.

🔍 Fetch any problem by its slug (URL-friendly name).

💻 Automatically save the question description, code template, and test cases for local testing and debugging.

🗂️ Build your own bank of solutions over time.

No more switching tabs. No more copy-pasting. Just focus on solving problems locally with your favorite tools and editor.

⚙️ Features<br/>
✅ Get Daily Challenge problem automatically <br/>
✅ Get any problem by slug (e.g. "two-sum", "longest-palindromic-substring") <br/>
✅ Save question, description, test cases, and starter code <br/>
✅ Work offline and test locally <br/>
✅ Build a local bank of solutions <br/>
✅ Fast and lightweight (uses requests + simple parsing) <br/>

📚 Why I Built This
As a regular LeetCoder, I wanted a smoother workflow:

Avoid browser distractions

Easily test edge cases offline

Version control my solutions in Git

Gradually build a personal solution bank for revision and reference

I hope this helps other programmers who want to level up their algorithm skills!

Contributions are welcome (scrapper, test suite, question bank, etc ).

> [!NOTE]
> Some codes are gathered from internet and not all of them are not my original work.

📦 How to Use

### Getting Questions

First, install requirements:

```shell
pip install -r requirements.txt -U 
```

To get any question, with problem and description, use download command.

```shell
python main.py -d
```
or
```shell
python main.py --daily
```

and to get any other, use:

```shell
python main.py -s `QUESTION_SLUG`
```
or
```shell
python main.py --slug `QUESTION_SLUG`
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

<!-- leetcode scraper, leetcode offline practice, leetcode cli, leetcode downloader, leetcode python tool,
fetch leetcode questions, local leetcode testing, competitive programming tools, leetcode daily challenge fetcher,
leetcode solution bank -->


