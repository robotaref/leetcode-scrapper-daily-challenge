from functools import cache
from typing import List

from solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.mostPoints
        self.questions = []

    @cache
    def getBest(self, index) -> int:
        if index >= len(self.questions):
            return 0
        a1 = self.getBest(index + self.questions[index][1] + 1) + self.questions[index][0]
        a2 = self.getBest(index + 1)
        return max(a1, a2)

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.questions = questions
        return self.getBest(0)


BaseSolutionTest(Solution, used_tests=[1])
