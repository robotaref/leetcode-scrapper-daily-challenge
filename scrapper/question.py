class Question:
    id = None
    title = None
    difficulty = None
    slug = None
    content = None
    editor_data = None
    test_cases = None
    outputs = []
    inputs = []
    main_method = None

    def __init__(self, slug):
        self.slug = slug

    def set_title(self, idx, title, difficulty):
        self.id = idx
        self.title = title
        self.difficulty = difficulty

    def set_main_method_name(self, main_method):
        self.main_method = main_method

    def set_outputs(self, outputs):
        self.outputs = outputs

    def set_contents(self, content):
        self.content = content

    def set_editor_data(self, editor_data):
        self.editor_data = editor_data

    def set_test_cases(self, test_cases):
        self.test_cases = test_cases

    def set_inputs(self, inputs):
        self.inputs = inputs
