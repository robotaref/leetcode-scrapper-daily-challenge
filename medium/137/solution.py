from collections import Counter
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.singleNumber


BaseSolutionTest(TestableSolution, )
