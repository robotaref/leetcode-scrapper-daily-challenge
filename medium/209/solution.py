from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = sum(nums)
        if s < target:
            return 0
        if s == target:
            return len(nums)
        nums.sort()
        nums.reverse()
        start = 0
        end = len(nums)
        p = end
        while start < end - 1:
            p = (end + start) // 2
            s = sum(nums[:p])
            if s < target:
                start = p
            else:
                end = p
        print(p)
        if sum(nums[:p]) <= target:
            print(sum(nums[:p], target))
            return p
        return p - 1


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.minSubArrayLen


BaseSolutionTest(TestableSolution, )
