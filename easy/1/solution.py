from testing.solution_test import BaseSolutionTest


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		return


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.twoSum


BaseSolutionTest(TestableSolution, )
