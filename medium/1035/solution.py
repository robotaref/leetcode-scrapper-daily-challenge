from functools import cache
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.maxUncrossedLines

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)

        @cache
        def calculateMax(index1, index2):
            if index1 == N1 or index2 == N2:
                return 0
            best = 0
            if nums1[index1] == nums2[index2]:
                best = calculateMax(index1 + 1, index2 + 1) + 1

            return max(best, calculateMax(index1, index2 + 1), calculateMax(index1 + 1, index2))

        return calculateMax(0, 0)


BaseSolutionTest(Solution())
