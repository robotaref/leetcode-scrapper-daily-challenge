from testing.solution_test import BaseSolutionTest


class Solution:
	def answerString(self, word: str, numFriends: int) -> str:
		return


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.answerString


BaseSolutionTest(TestableSolution, )
