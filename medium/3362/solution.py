from testing.solution_test import BaseSolutionTest
from typing import List


class Solution:
	def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
		diff = [0] * len(queries)
		for i in range(len(diff)):
			diff[i] = queries[i][1] - queries[i][0]

		counter = len(queries)
		queries = [x for _,x in sorted(zip(diff, queries), reverse=True)]
		for query in queries:
			for i in range(query[0], query[1]+1):
				nums[i] = 0 if nums[i] == 0 else nums[i] - 1
			counter -= 1
			if not any(nums):
				return counter
		return -1


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.maxRemoval


BaseSolutionTest(TestableSolution, )
