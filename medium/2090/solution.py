from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        q = 0
        res = []
        for i, num in enumerate(nums):
            if i < k:
                res.append(-1)
            q += num
            if i > 2 * k:
                q -= nums[i - 2 * k-1]
            if i >= 2 * k:
                res.append(q // (2 * k + 1))
        n = max(len(nums) - len(res), 0)
        res = res + [-1] * n

        return res


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.getAverages


BaseSolutionTest(TestableSolution, )
