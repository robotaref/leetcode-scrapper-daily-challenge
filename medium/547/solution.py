from collections import defaultdict, deque
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.isConnected = [[]]
        self.colored = []
        self.n = 0

    def color(self, i, d):
        self.colored[i] = d
        for j, c in enumerate(self.isConnected[i]):
            if i != j and c == 1 and not self.colored[j]:
                self.color(j, d)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)
        self.isConnected = isConnected
        self.colored = [False] * self.n
        c = 0
        for i in range(self.n):
            if not self.colored[i]:
                c += 1
                self.color(i, c)
        return c


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.findCircleNum


BaseSolutionTest(TestableSolution)
