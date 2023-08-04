from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        print(length)
        print(count)
        max_length = max(length)
        result = 0

        for i in range(n):
            if length[i] == max_length:
                result += count[i]

        return result


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.findNumberOfLIS


BaseSolutionTest(TestableSolution, )
