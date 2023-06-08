from collections import defaultdict
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(n):
            graph[manager[i]].append(i)

        def get_time(i):
            if len(graph[i]) == 0:
                return 0
            m = 0
            for worker in graph[i]:
                m = max(m, get_time(worker) + informTime[i])
            return m

        return get_time(headID)


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.numOfMinutes


BaseSolutionTest(TestableSolution)
