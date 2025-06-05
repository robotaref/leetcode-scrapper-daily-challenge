from testing.solution_test import BaseSolutionTest
from typing import List

import numpy as np


class Solution:
	def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
		return


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.minZeroArray


BaseSolutionTest(TestableSolution, )
