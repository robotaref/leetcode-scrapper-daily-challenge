import bisect
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0
        last_position = 0
        for i in range(m):
            grid[i].reverse()
            last_position = (bisect.bisect_left(grid[i], 0, last_position, n))
            c += last_position
        return c


class TestableSolution(Solution):
    def __init__(self):
        self.main = self.countNegatives


BaseSolutionTest(TestableSolution, )
