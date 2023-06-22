from typing import List

from math import comb

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.mod = 10 ** 9 + 7

    def count(self, arr):
        m = len(arr)
        if m < 3:
            return 1
        left = [a for a in arr[1:] if a < arr[0]]
        right = [a for a in arr[1:] if a > arr[0]]
        return self.count(left) * self.count(right) * comb(m - 1, len(left)) % self.mod

    def numOfWays(self, nums: List[int]) -> int:
        return (self.count(nums) - 1) % self.mod


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.numOfWays


BaseSolutionTest(TestableSolution, )
