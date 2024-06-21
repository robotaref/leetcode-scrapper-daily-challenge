from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sat = 0
        for c, g in zip(customers, grumpy):
            sat += c * (1 - g)
        new = 0
        for c, g in zip(customers[:minutes], grumpy[:minutes]):
            new += c * g
        best = sat + new
        for i in range(0, len(grumpy) - minutes):
            new += - grumpy[i] * customers[i] + (grumpy[i + minutes] * customers[i + minutes])
            best = max(sat + new, best)
        return best


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.maxSatisfied


BaseSolutionTest(TestableSolution, )
