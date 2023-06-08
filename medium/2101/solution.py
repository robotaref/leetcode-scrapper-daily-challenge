from collections import defaultdict
from functools import cache
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.bombs = []
        self.detonated = []
        self.adj_bombs = defaultdict(list)

    @cache
    def get_distance(self, i, j):
        return (self.bombs[i][0] - self.bombs[j][0]) ** 2 + (self.bombs[i][1] - self.bombs[j][1]) ** 2

    def detonate_bomb(self, i):
        self.detonated[i] = True
        s = 1
        for j in (self.adj_bombs[i]):
            if not self.detonated[j]:
                s += self.detonate_bomb(j)
        return s

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        self.bombs = bombs
        for i in range(n):
            for j in range(n):
                if i != j:
                    if self.get_distance(min(i, j), max(i, j)) <= self.bombs[i][2] ** 2:
                        self.adj_bombs[i].append(j)
        s = 0
        for i in range(n):
            self.detonated = [False] * n
            s = max(s, self.detonate_bomb(i))
        return s


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.maximumDetonation


BaseSolutionTest(TestableSolution)
