import heapq
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.maxScore
        self.questions = []

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        points = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
        points.sort(key=lambda x: -x[1])
        h = [i[0] for i in points[:k]]
        heapq.heapify(h)
        s = sum(h)
        m = s * points[k - 1][1]
        for i in range(k, n):
            a = heapq.heappop(h)
            s -= a
            s += points[i][0]
            m = max(points[i][1] * s, m)
            heapq.heappush(h, points[i][0])

        return m


BaseSolutionTest(Solution, )
