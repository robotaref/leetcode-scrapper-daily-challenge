from typing import List
from testing.solution_test import BaseSolutionTest


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		for i in range(nums.count(val)):
			nums.pop(nums.index(val))
		return len(nums), 


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.removeElement


BaseSolutionTest(TestableSolution, )
