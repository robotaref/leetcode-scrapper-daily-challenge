import collections
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        return [i for i, j in collections.Counter(nums).most_common(k)]


class TestableSolution(Solution):
    def __init__(self):
        self.main = self.topKFrequent


BaseSolutionTest(TestableSolution)
