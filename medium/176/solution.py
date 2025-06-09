from testing.solution_test import BaseSolutionTest


import pandas as pd

class Solution:
	def second_highest_salary(self, employee: pd.DataFrame) -> pd.DataFrame:
		u_sorted = sorted(employee.salary.unique(), reverse=True)
		if len(u_sorted) >= 2:
			return pd.DataFrame([u_sorted[1]], columns=["SecondHighestSalary"])
		else:
			return pd.DataFrame([None], columns=["SecondHighestSalary"])


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.second_highest_salary


BaseSolutionTest(TestableSolution, )
