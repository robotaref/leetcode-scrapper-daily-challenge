from functools import cache
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        num_and_cost = sorted([num, c] for num, c in zip(nums, cost))
        n = len(cost)

        prefix_cost = [0] * n
        prefix_cost[0] = num_and_cost[0][1]
        for i in range(1, n):
            prefix_cost[i] = num_and_cost[i][1] + prefix_cost[i - 1]

        total_cost = 0
        for i in range(1, n):
            total_cost += num_and_cost[i][1] * (num_and_cost[i][0] - num_and_cost[0][0])
        answer = total_cost

        for i in range(1, n):
            gap = num_and_cost[i][0] - num_and_cost[i - 1][0]
            total_cost += prefix_cost[i - 1] * gap
            total_cost -= gap * (prefix_cost[n - 1] - prefix_cost[i - 1])
            answer = min(answer, total_cost)

        return answer


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.minCost


BaseSolutionTest(TestableSolution, )
