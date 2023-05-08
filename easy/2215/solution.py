from typing import List

from base_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.main = self.findDifference

    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [[n for n in nums1 if n not in nums2], [n for n in nums2 if n not in nums1]]

    @staticmethod
    def findDifferenceMethod2(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [list(nums1 - nums2), list(nums2 - nums1)]


BaseSolutionTest(Solution())
