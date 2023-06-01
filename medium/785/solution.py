import collections
from typing import List

from base_test import BaseSolutionTest


class Solution:
    opponent = {}
    answers = {"R": "Radiant", "D": "Dire"}

    def __init__(self):
        self.main = self.isBipartite

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color_map = {}

        def dfs(i, color):
            color_map[i] = color
            for g in graph[i]:
                n_color = color_map.get(g, None)
                if n_color and n_color == color:
                    return True
                if n_color is None:
                    r = dfs(g, -color)
                    if r:
                        return True

        for node, edges in enumerate(graph):
            if color_map.get(node, None) is None:
                is_paradox = dfs(node, 1)
                if is_paradox:
                    return False
        return True


BaseSolutionTest(Solution)