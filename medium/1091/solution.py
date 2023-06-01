from collections import deque, defaultdict
from functools import cache
from typing import List

from base_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.actions = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    self.actions.append((i, j))
        self.main = self.shortestPathBinaryMatrix

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        borders = deque([(0, 0, 0)])
        dp = [[0] * n for _ in range(n)]

        while len(borders) > 0:
            x, y, d = borders.popleft()
            if x == n - 1 and y == n - 1:
                return d + 1
            else:
                for dx, dy in self.actions:
                    new_x, new_y = x + dx, y + dy
                    if -1 < new_x < n and -1 < new_y < n and grid[new_x][new_y] == 0:
                        if dp[new_x][new_y] == 0:
                            borders.append((new_x, new_y, d + 1))
                            dp[new_x][new_y] = d + 1

        return -1


BaseSolutionTest(Solution)
