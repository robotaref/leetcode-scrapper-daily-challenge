from testing.solution_test import BaseSolutionTest


import pandas as pd

class Solution:
	def combine_two_tables(self, person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
		return pd.DataFrame([])


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.combine_two_tables


BaseSolutionTest(TestableSolution, )
