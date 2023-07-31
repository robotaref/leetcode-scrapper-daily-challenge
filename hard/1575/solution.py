from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
	def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
		return


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.countRoutes


BaseSolutionTest(TestableSolution, )
