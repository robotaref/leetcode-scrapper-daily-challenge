import collections
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid_t = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                grid_t[i][j] = grid[j][i]
        g = {}
        g_t = {}
        for i in range(n):
            g[i] = sum(grid[i])
            g_t[i] = sum(grid_t[i])
        c = 0
        for i in range(n):
            for j in range(n):
                if g[i] == g_t[j] and grid[i] == grid_t[j]:
                    c += 1
        return c

    def equalPairs2(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        # Keep track of the frequency of each row.
        row_counter = collections.Counter(tuple(row) for row in grid)

        # Add up the frequency of each column in map.
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

        return count


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.equalPairs2


BaseSolutionTest(TestableSolution, )
