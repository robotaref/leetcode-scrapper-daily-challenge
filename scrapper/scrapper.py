import ast
import json
import os
import re

import markdownify
import requests

from scrapper.question import Question


class Scrapper:
    url = "https://leetcode.com/graphql/"

    def call(self, data):
        response = requests.post(url=self.url, json=data)
        print("response status code: ", response.status_code)
        if response.status_code == 200:
            return response.json()

    @staticmethod
    def open_json(data_file_name):
        data_file = f"scrapper/assets/{data_file_name}.json"

        f = open(data_file)
        data = json.load(f)
        return data

    def get_from_api(self, data_file_name):
        raise NotImplementedError

    def scrape(self, ):
        raise NotImplementedError


class QuestionScrapper(Scrapper):
    question: Question = None

    def __init__(self, question_name):
        self.question_name = question_name
        self.imports_text = "from testing.solution_test import BaseSolutionTest\n\n\n"
        self.base_editor_text = "return\n\n\nclass TestableSolution(Solution):" + \
                                "\n\tdef __init__(self):\n\t\tsuper().__init__()\n\t\t" \
                                "self.main = self.{function_name}\n"
        self.base_test_text = """\n\nBaseSolutionTest(TestableSolution, )\n"""

    def get_from_api(self, data_file_name):
        data = self.open_json(data_file_name)
        data["variables"]["titleSlug"] = self.question.slug
        return self.call(data)["data"]["question"]

    def get_difficulty(self):
        res = self.get_from_api("questionTitle")
        idx = res["questionFrontendId"]
        title = res["title"]
        difficulty = res["difficulty"]
        self.question.set_title(idx, title, difficulty)

    def get_question_contents(self):
        res = self.get_from_api("questionContent")
        content = res["content"]
        self.question.set_outputs(re.findall(r"(?<=<strong>Output:</strong> )(.*)(?=\n)", content))
        content = f"<h2>{self.question.id}. {self.question.title}</h2>\n\n" + content
        h = markdownify.markdownify(content, heading_style="ATX", escape_underscores=False)
        self.question.set_contents(h)

    def get_console_panel_config(self):
        res = self.get_from_api("consolePanelConfig")
        method_meta_data = json.loads(res["metaData"])
        try:

            name_ = method_meta_data["name"]
        except:
            name_ = "test"
        self.question.set_main_method_name(name_)

        example_testcase_list_ = res["exampleTestcaseList"]
        print(method_meta_data)
        print(example_testcase_list_)
        inputs = {}
        for i, case in enumerate(example_testcase_list_):
            t = {}
            case_split = case.split("\n")
            for j, param in enumerate(method_meta_data["params"]):
                t[param["name"]] = ast.literal_eval(case_split[j].replace("null", "None"))
            try:
                inputs[f"question_{i + 1}"] = {"input": t, "output": self.parse_output(self.question.outputs[i])}
            except ValueError as e:
                print(f"'{self.question.outputs[i]}' can't be parsed with error {repr(e)}")
        self.question.set_inputs(inputs)

    @staticmethod
    def parse_output(output: str):
        if output == "true":
            return True
        if output == "false":
            return False
        output = output.replace("&quot;", '"')
        try:
            return ast.literal_eval(output)
        except Exception as e:
            print(f"could not parse output {output}, error: {repr(e)}")
            return output

    def get_question_editor_data(self):
        res = self.get_from_api("questionEditorData")

        for row in (res["codeSnippets"]):
            if row["lang"] == "Python3":
                editor_data = row["code"].replace("    ", "\t")
                editor_data = self.imports_text + editor_data + self.base_editor_text.format(
                    function_name=self.question.main_method) + self.base_test_text
                self.question.set_editor_data(editor_data)

    def make_files(self):
        base_address = os.path.join(self.question.difficulty.lower(), self.question.id)

        os.makedirs(base_address)
        print(f"files were created in {base_address}")
        read_me_address = os.path.join(base_address, "readme.md")
        f = open(read_me_address, "w")
        f.write(self.question.content)
        f.close()

        solution_file_address = os.path.join(base_address, "solution.py")
        f = open(solution_file_address, "w")
        f.write(self.question.editor_data)
        f.close()

        test_cases_address = os.path.join(base_address, "test_cases.json")
        f = open(test_cases_address, "w")
        json.dump(self.question.inputs, f)
        f.close()

    def scrape(self):
        self.question = Question(self.question_name)
        self.get_difficulty()
        self.get_question_contents()
        self.get_console_panel_config()
        self.get_question_editor_data()
        self.make_files()


class DailyChallengeScrapper(Scrapper):
    question_slug: str = ""

    def get_from_api(self, data_file_name):
        data = self.open_json(data_file_name)
        return self.call(data)

    def scrape(self):
        self.question_slug = self.get_daily_question_slug()

    def get_daily_question_slug(self):
        res = self.get_from_api("questionOfToday")
        slug = res["data"]["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]
        print(f"today's question: https://leetcode.com/problems/{slug}/")
        return slug
