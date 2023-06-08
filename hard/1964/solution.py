from bisect import bisect_right
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        tail = []

        for obstacle in obstacles:
            if not tail or obstacle >= tail[-1]:
                tail.append(obstacle)
                ans.append(len(tail))
            else:
                index = bisect_right(tail, obstacle)
                tail[index] = obstacle
                ans.append(index + 1)

        return ans


class TestableSolution(Solution):
    def __init__(self):
        self.main = self.longestObstacleCourseAtEachPosition


BaseSolutionTest(TestableSolution)
