from testing.solution_test import BaseSolutionTest


class Solution:
	def differenceOfSums(self, n: int, m: int) -> int:
		sums = n * (n + 1) / 2

		c_sums = n * (n + 1) / 2

		for i in range(1, n+1):
			if i % m == 0:
				c_sums -= i

		return int(c_sums - sums + c_sums)


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.differenceOfSums


BaseSolutionTest(TestableSolution, )
