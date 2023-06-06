from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.main = self.canMakeArithmeticProgression

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        for i in range(n - 2):
            if arr[i + 2] - arr[i + 1] != arr[i + 1] - arr[i]:
                return False
        return True


BaseSolutionTest(Solution, )
