from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        a = nums[0]
        n = len(nums)
        res = []
        b = nums[0]
        for x, y in zip(nums[:n], nums[1:]):
            if x != y - 1:
                if a == x:
                    res.append(str(a))
                else:
                    res.append(f"{str(a)}->{str(x)}")
                a = y
            b = y
        if a == b:
            res.append(str(a))
        else:
            res.append(f"{str(a)}->{str(y)}")
        return res


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.summaryRanges


BaseSolutionTest(TestableSolution, )
