from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        return 0


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.maximumDetonation


BaseSolutionTest(TestableSolution)
