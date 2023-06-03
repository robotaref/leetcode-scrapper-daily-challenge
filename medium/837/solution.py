from functools import lru_cache

from testing.solution_test import ApproximateSolutionTest


class Solution:

    def __init__(self):
        self.main = self.new21Game
        self.n = 0
        self.k = 0
        self.maxPts = 0

    @lru_cache
    def get_probability(self, start_i):
        if start_i > self.n:
            return 0
        if self.k <= start_i <= self.n:
            return 1
        else:
            p = []
            for i in range(start_i + 1, start_i + self.maxPts + 1):
                p.append(1 / self.maxPts * self.get_probability(i))
        return sum(p)

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        self.n = n
        self.k = k
        self.maxPts = maxPts
        return self.get_probability(max(0, self.k - self.maxPts))


ApproximateSolutionTest(Solution)
