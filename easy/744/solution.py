import bisect
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect_right(letters, target)
        if i == len(letters):
            return letters[0]
        return letters[i]


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.nextGreatestLetter


BaseSolutionTest(TestableSolution, )
