import collections
from typing import List, Set

from solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.calcEquation

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[
        float]:
        ans = []
        graph = collections.defaultdict(dict)

        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value

        def divide(A: str, C: str, seen: Set[str]) -> float:
            if A == C:
                return 1.0

            seen.add(A)

            for B, value in graph[A].items():
                if B in seen:
                    continue
                res = divide(B, C, seen)
                if res > 0:
                    return value * res

            return -1.0

        for A, C in queries:
            if A not in graph and C not in graph:
                ans.append(-1.0)
            else:
                ans.append(divide(A, C, set()))

        return ans


BaseSolutionTest(Solution,)
