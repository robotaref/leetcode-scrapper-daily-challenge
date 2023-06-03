from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.findSmallestSetOfVertices

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        start_nodes, end_nodes = [], []
        for x, y in edges:
            start_nodes.append(x)
            end_nodes.append(y)
        start_nodes = set(start_nodes)
        end_nodes = set(end_nodes)
        return list(start_nodes - end_nodes)


BaseSolutionTest(Solution, )
