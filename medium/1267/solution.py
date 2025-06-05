from typing import List
from testing.solution_test import BaseSolutionTest


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        total_servers = sum(sum(grid, []))

        for row in range(rows):
            if sum(grid[row]) == 1:
                for column in [i for i, e in enumerate(grid[row]) if e != 0]:
                    if sum([row[column] for row in grid]) == 1:
                        total_servers -= 1
        return total_servers


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.countServers


BaseSolutionTest(TestableSolution, )
