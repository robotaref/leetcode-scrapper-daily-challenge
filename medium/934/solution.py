from typing import List

from base_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.shortestBridge
        self.is_seen = []
        self.bfs_is_seen = []
        self.color = []
        self.grid = None
        self.n = 0
        self.color_place = {}

    def dfs(self, i, j, color):
        if min(i, j) < 0 or max(i, j) >= self.n:
            return
        if self.is_seen[i][j]:
            return
        self.is_seen[i][j] = 1

        if self.grid[i][j] == 1:
            self.color[i][j] = color
            self.color_place[color].append((i, j))
            self.dfs(i - 1, j, color)
            self.dfs(i + 1, j, color)
            self.dfs(i, j + 1, color)
            self.dfs(i, j - 1, color)

    def bfs(self, front):
        new_front = []
        for i, j in front:
            if min(i, j) < 0 or max(i, j) >= self.n:
                front.append((i, j))

    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.grid = grid
        self.is_seen = [[0] * self.n for _ in range(self.n)]
        self.color = [[0] * self.n for _ in range(self.n)]
        self.d_color = [[0] * self.n for _ in range(self.n)]
        color = 1
        for i in range(self.n):
            for j in range(self.n):
                if self.color[i][j] == 0 and self.grid[i][j] == 1:
                    self.color_place[color] = []
                    self.dfs(i, j, color)
                    color += 1
        l = self.n
        for x, y in self.color_place[2]:
            for i, j in self.color_place[1]:
                l = min(l, abs(i - x) + abs(j - y) - 1)
        return l


BaseSolutionTest(Solution)
