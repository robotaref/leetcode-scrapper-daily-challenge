from typing import Union


class Question:
    id: str = None
    title: str = None
    difficulty: str = None
    slug: str = None
    topic_tags = None
    content: str = None
    editor_data: str = None
    test_cases: dict = {}
    outputs: dict = {}
    inputs: dict = {}
    main_method: str = None

    def __init__(self, slug: str):
        self.slug = slug

    def set_title(self, idx: str, title: str, difficulty: str):
        self.id = idx
        self.title = title
        self.difficulty = difficulty

    def set_main_method_name(self, main_method: str):
        self.main_method = main_method

    def set_outputs(self, outputs: Union[dict, list]):
        self.outputs = outputs

    def set_contents(self, content: str):
        self.content = content

    def set_editor_data(self, editor_data: str):
        self.editor_data = editor_data

    def set_test_cases(self, test_cases: dict):
        self.test_cases = test_cases

    def set_inputs(self, inputs: dict):
        self.inputs = inputs

    def set_topic_tags(self, tags: list):
        self.topic_tags = tags
