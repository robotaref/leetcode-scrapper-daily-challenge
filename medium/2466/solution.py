from solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.countGoodStrings

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        kMod = 1_000_000_007
        ans = 0
        dp = {0: 1}
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp.get(i, 0) + dp.get(i - zero, 0)) % kMod
            if i >= one:
                dp[i] = (dp.get(i, 0) + dp.get(i - one, 0)) % kMod
            if i >= low:
                ans = (ans + dp[i]) % kMod
        return ans


BaseSolutionTest(Solution, )
