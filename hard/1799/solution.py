from typing import List

from math import gcd

from testing.solution_test import BaseSolutionTest


class Solution:

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (1 << n)

        def dfs(mask, t):
            if mask == (1 << n) - 1:
                return 0
            if dp[mask] != -1:
                return dp[mask]
            ma = 0
            for i in range(n):
                if (1 << i) & mask:
                    continue
                for j in range(i + 1, n):
                    if (1 << j) & mask:
                        continue
                    next = dfs(mask | (1 << i) | (1 << j), t + 1) + gcd(nums[i], nums[j]) * t
                    ma = max(next, ma)
            dp[mask] = ma
            return dp[mask]

        return dfs(0, 1)


class TestableSolution(Solution):
    def __init__(self):
        self.main = self.maxScore


BaseSolutionTest(TestableSolution)
