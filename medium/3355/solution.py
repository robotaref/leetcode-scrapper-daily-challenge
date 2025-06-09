import numpy as np

from testing.solution_test import BaseSolutionTest
from typing import List


class Solution:
	def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
		if not any(nums):
			return True

		check_array = np.zeros(len(nums))

		for q in queries:
			if q[0] == q[1]:
				check_array[q[0]] += 1
			else:
				check_array[q[0]:q[1] + 1] += 1

		if not all(check_array >= nums):
			return False

		return True


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.isZeroArray


BaseSolutionTest(TestableSolution, )
