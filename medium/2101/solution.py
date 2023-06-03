from functools import cache
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.main = self.maximumDetonation
        self.bombs = []
        self.detonated = []

    @cache
    def get_distance(self, i, j):
        return (self.bombs[i][0] - self.bombs[j][0]) ** 2 + (self.bombs[i][1] - self.bombs[j][1]) ** 2

    def detonate_bomb(self, i):
        self.detonated[i] = True
        s = 1
        for j, bomb in enumerate(self.bombs):
            if not self.detonated[j]:
                if self.get_distance(min(i, j), max(i, j)) <= self.bombs[i][2] ** 2:
                    s += self.detonate_bomb(j)
        return s

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        self.bombs = bombs

        s = 0
        for i in range(n):
            self.detonated = [False] * n
            s = max(s, self.detonate_bomb(i))
        return s


BaseSolutionTest(Solution, )
