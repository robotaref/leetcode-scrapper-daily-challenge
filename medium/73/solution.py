from testing.solution_test import BaseSolutionTest
from typing import List


class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
		m = len(matrix)
		n = len(matrix[0])

		cols = []

		for i in range(m):
			if 0 in matrix[i]:
				for j in range(n):
					if matrix[i][j] == 0:
						cols.append(j)
				matrix[i] = [0] * n

		for i in cols:
			for k in range(m):
				matrix[k][i] = 0

		return matrix


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.setZeroes


BaseSolutionTest(TestableSolution, )
