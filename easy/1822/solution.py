from typing import List

from base_test import BaseSolutionTest


class Solution:
    def __init__(self):

        self.main = self.arraySign

    @staticmethod
    def arraySign(nums: List[int]) -> int:
        num_negative = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                num_negative += 1

        if num_negative % 2 == 0:
            return 1
        return -1


BaseSolutionTest(Solution())
