from functools import cache
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.grid = []
        self.n = 0
        self.m = 0
        self.mod = 10 ** 9 + 7
        self.actions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    @cache
    def count(self, i, j):
        c = 1
        for x, y in self.actions:
            new_x = i + x
            new_y = j + y
            if 0 <= new_x < self.n and 0 <= new_y < self.m:
                if self.grid[new_x][new_y] > self.grid[i][j]:
                    c += self.count(new_x, new_y)
        return c % self.mod

    def countPaths(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        c = 0
        for i in range(self.n):
            for j in range(self.m):
                c += self.count(i, j)
        return c % self.mod


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.countPaths


BaseSolutionTest(TestableSolution, )
