from typing import List
from testing.solution_test import BaseSolutionTest
from collections import deque
from itertools import product

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        columns = len(isWater[0])

        queue = deque()
        visited = [[False] * columns for _ in range(rows)]
        heights = [[0] * columns for _ in range(rows)]
        for row, col in product(range(rows), range(columns)):
            if isWater[row][col] == 1:
                queue.append((row, col))
                heights[row][col] = 0
                visited[row][col] = True
        while queue:
            r, c = queue.popleft()
            for row, col in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):  # all directions
                if 0 <= row < rows and 0 <= col < columns and not visited[row][col]:
                    heights[row][col] = heights[r][c] + 1
                    visited[row][col] = True
                    queue.append((row, col))

        return heights


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.highestPeak


BaseSolutionTest(TestableSolution, )
