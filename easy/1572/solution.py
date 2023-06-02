from typing import List

from solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.main = self.diagonalSum

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        d1 = [mat[i][i] + mat[i][n - 1 - i] for i in range(n)]
        d1 = sum(d1)
        if n % 2 == 1:
            d1 -= mat[n // 2][n // 2]
        return d1


BaseSolutionTest(Solution())
