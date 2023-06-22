from functools import cache
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.fee = 0
        self.prices = []

    @cache
    def getMaxProfit(self, i):
        p = 0
        if i == len(self.prices) - 1:
            return 0
        for j in range(i + 1, len(self.prices)):
            cur_p = self.getMaxProfit(j)
            d = self.prices[j] - self.prices[i] - self.fee
            if d > 0:
                cur_p += d
            p = max(p, cur_p)
        return p

    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.prices = prices
        self.fee = fee
        return self.getMaxProfit(0)


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.maxProfit


BaseSolutionTest(TestableSolution, )
