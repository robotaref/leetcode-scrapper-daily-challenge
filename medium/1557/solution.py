from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        start_nodes, end_nodes = [], []
        for x, y in edges:
            start_nodes.append(x)
            end_nodes.append(y)
        start_nodes = set(start_nodes)
        end_nodes = set(end_nodes)
        return list(start_nodes - end_nodes)


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.findSmallestSetOfVertices


BaseSolutionTest(TestableSolution)
