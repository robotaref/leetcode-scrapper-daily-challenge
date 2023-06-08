from collections import deque
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    modul = (10 ** 9 + 7)
    two_powers = {0: 1}

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = self.filter_larger_than_target(nums, target)
        nums.sort()
        nums = deque(nums)
        cnt = 0
        for i in range(len(nums)):
            self.two_powers[i + 1] = self.two_powers[i] * 2
        while len(nums) > 0:
            if nums[0] + nums[-1] <= target:
                cnt += self.two_powers[len(nums) - 1] % self.modul
                nums.popleft()
            else:
                nums.pop()

        return cnt % self.modul

    @staticmethod
    def filter_larger_than_target(nums, target):
        return [n for n in nums if n < target]


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.numSubseq


BaseSolutionTest(TestableSolution)
