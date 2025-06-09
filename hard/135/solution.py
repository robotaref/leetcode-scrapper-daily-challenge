from testing.solution_test import BaseSolutionTest


class Solution:
	def candy(self, ratings: List[int]) -> int:
		return


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.candy


BaseSolutionTest(TestableSolution, )
