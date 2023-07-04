from functools import cache
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.fee = 0
        self.prices = []
        self.n = 0

    @cache
    def should_check(self, i):
        if i == self.n - 1:
            return True
        if self.prices[i - 1] < self.prices[i] < self.prices[i + 1]:
            return False
        if self.prices[i - 1] > self.prices[i] > self.prices[i + 1]:
            return False
        return True

    @cache
    def getMaxProfit(self, i):
        p = 0
        if i == self.n - 1:
            return 0
        for j in range(i + 1, self.n):
            if self.should_check(j):
                cur_p = self.getMaxProfit(j)
                d = self.prices[j] - self.prices[i] - self.fee
                if d > 0:
                    cur_p += d
                p = max(p, cur_p)
        return p

    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.prices = prices
        self.fee = fee
        self.n = len(self.prices)

        return self.getMaxProfit(0)


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.maxProfit


BaseSolutionTest(TestableSolution, )
