import collections
from typing import List

from solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.topKFrequent

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i, j in collections.Counter(nums).most_common(k)]


BaseSolutionTest(Solution, )
