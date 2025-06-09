import ast
import json
import os
import re

import markdownify
import requests


from typing import Union
from .question import Question
from .utils import open_json, json2dataframe, str2dataframe, wrap_in_solution_class, parse_output

IMPORT_TEXT = "from testing.solution_test import BaseSolutionTest\n\n\n"

BASE_EDITOR_TEXT = "return\n\n\nclass TestableSolution(Solution):" + \
                   "\n\tdef __init__(self):\n\t\tsuper().__init__()\n\t\t" \
                   "self.main = self.{function_name}\n"

BASE_TEST_TEXT = """\n\nBaseSolutionTest(TestableSolution, )\n"""


class Scrapper:
    url = "https://leetcode.com/graphql/"
    question = None

    def call(self, data: dict) -> dict:
        response = requests.post(url=self.url, json=data)
        print("response status code: ", response.status_code)
        if response.status_code == 200:
            return response.json()

    def get_from_api(self, data_file_name: Union[str, dict]) -> dict:
        raise NotImplementedError

    def scrape(self, slug: str = None, daily: bool = False) -> None:
        raise NotImplementedError

    def content2output(self, content: str) -> Union[list, dict]:
        # scrape outputs based on topic tags
        if "database" in self.question.topic_tags:
            output = re.findall(r'<strong>Output:</strong> \n(.*?)\n<', content, re.S)
            return [str2dataframe(case) for case in output]
        else:
            return re.findall(r"(?<=<strong>Output:</strong> )(.*)(?=\n)", content)


class QuestionScrapper(Scrapper):
    def __init__(self):
        self.imports_text = IMPORT_TEXT
        self.base_editor_text = BASE_EDITOR_TEXT
        self.base_test_text = BASE_TEST_TEXT

    def get_from_api(self, data_file_name: Union[str, dict]) -> dict:
        data = open_json(data_file_name)
        data["variables"]["titleSlug"] = self.question.slug
        return self.call(data)["data"]["question"]

    def get_difficulty(self) -> None:
        res = self.get_from_api("questionTitle")
        idx = res["questionFrontendId"]
        title = res["title"]
        difficulty = res["difficulty"]
        self.question.set_title(idx, title, difficulty)

    def get_question_topic_tags(self) -> None:
        res = self.get_from_api("topic_tags")
        self.question.set_topic_tags([tag['slug'] for tag in res["topicTags"]])

    def get_question_contents(self) -> None:
        res = self.get_from_api("questionContent")
        # set outputs
        content = res["content"]
        self.question.set_outputs(self.content2output(content))
        # set contents
        content = f"<h2>{self.question.id}. {self.question.title}</h2>\n\n" + content
        h = markdownify.markdownify(content, heading_style="ATX", escape_underscores=False)
        self.question.set_contents(h)

    def get_console_panel_config(self) -> None:
        res = self.get_from_api("consolePanelConfig")
        method_meta_data = json.loads(res["metaData"])

        self.question.set_main_method_name(method_meta_data["name"]) if 'name' in method_meta_data \
            else self.question.set_main_method_name("test")

        example_testcase_list_ = res["exampleTestcaseList"]
        print(method_meta_data)
        print(example_testcase_list_)

        inputs = {}
        for i, case in enumerate(example_testcase_list_):
            t = {}

            if "database" in method_meta_data and method_meta_data["database"]:
                t = json2dataframe(case)
                inputs[f"question_{i + 1}"] = {"input": t, "output": self.question.outputs[i]}

            elif "params" in method_meta_data:
                case_split = case.split("\n")
                for j, param in enumerate(method_meta_data["params"]):
                    t[param["name"]] = ast.literal_eval(case_split[j].replace("null", "None"))
                try:
                    inputs[f"question_{i + 1}"] = {"input": t, "output": parse_output(self.question.outputs[i])}
                except ValueError as e:
                    print(f"'{self.question.outputs[i]}' can't be parsed with error {repr(e)}")

        self.question.set_inputs(inputs)

    def get_question_editor_data(self) -> None:
        res = self.get_from_api("questionEditorData")
        for row in (res["codeSnippets"]):
            if row["lang"] == "Python3":
                editor_data = row["code"].replace("    ", "\t")
                editor_data = self.imports_text + editor_data + self.base_editor_text.format(
                    function_name=self.question.main_method) + self.base_test_text
                self.question.set_editor_data(editor_data)
            elif row["lang"] == "Pandas":
                editor_data = row["code"].replace("    ", "\t")
                editor_data = self.imports_text + wrap_in_solution_class(
                    editor_data) + self.base_editor_text.format(
                    function_name=self.question.main_method) + self.base_test_text
                self.question.set_editor_data(editor_data)

    def make_files(self) -> None:
        base_address = os.path.join(self.question.difficulty.lower(), self.question.id)
        if not os.path.exists(base_address):
            os.makedirs(base_address)
            print(f"files were created in {base_address}")
        else:
            print("directory already exists")

        read_me_address = os.path.join(base_address, "readme.md")
        if not os.path.isfile(read_me_address):
            f = open(read_me_address, "w")
            f.write(self.question.content + "\n" + str(self.question.topic_tags))
            f.close()
        else:
            print("readme already exists")

        solution_file_address = os.path.join(base_address, "solution.py")
        if not os.path.isfile(solution_file_address):
            f = open(solution_file_address, "w")
            f.write(self.question.editor_data)
            f.close()
        else:
            print("solution already exists")

        test_cases_address = os.path.join(base_address, "test_cases.json")
        if not os.path.isfile(test_cases_address):
            f = open(test_cases_address, "w")
            if "database" in self.question.topic_tags:
                to_dump = {}
                for item in self.question.inputs:
                    params = {}
                    for param in self.question.inputs[item]["input"]:
                        params[param] = self.question.inputs[item]["input"][param].to_json()
                    to_dump[item] = {"input": params, "output": self.question.inputs[item]["output"].to_json()}

                json.dump(to_dump, f, separators=(',', ':'))
            else:
                json.dump(self.question.inputs, f)

            f.close()
        else:
            print("test_cases already exists")

    def scrape(self, question_name: str = None, daily: bool = False):
        self.question = Question(question_name)
        self.get_difficulty()
        self.get_question_topic_tags()
        self.get_question_contents()
        self.get_console_panel_config()
        self.get_question_editor_data()
        self.make_files()


class DailyChallengeScrapper(QuestionScrapper):
    def get_from_api(self, data_file_name: Union[str, dict]) -> dict:
        data = open_json(data_file_name)
        if data_file_name == "questionOfToday":
            return self.call(data)
        else:
            data["variables"]["titleSlug"] = self.question.slug
            return self.call(data)["data"]["question"]

    def get_daily_question_slug(self) -> str:
        res = self.get_from_api("questionOfToday")
        slug = res["data"]["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]
        print(f"today's question: https://leetcode.com/problems/{slug}/")
        return slug

    def scrape(self, question_name: str = None, daily: bool = True) -> None:
        self.question = Question(self.get_daily_question_slug())
        self.get_difficulty()
        self.get_question_topic_tags()
        self.get_question_contents()
        self.get_console_panel_config()
        self.get_question_editor_data()
        self.make_files()
