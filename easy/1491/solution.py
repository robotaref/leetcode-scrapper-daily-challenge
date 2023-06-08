from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:

    @staticmethod
    def average(salary: List[int]) -> float:
        mini = min(salary)
        maxi = max(salary)
        r_salary = [s for s in salary if s not in [mini, maxi]]
        return sum(r_salary) / len(r_salary)


class TestableSolution(Solution):
    def __init__(self):
        self.main = self.average


BaseSolutionTest(TestableSolution)
