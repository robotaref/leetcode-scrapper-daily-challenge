from testing.solution_test import BaseSolutionTest
from typing import List


class Solution:
	def findWordsContaining(self, words: List[str], x: str) -> List[int]:
		words_with_x = []
		for i in range(len(words)):
			if x in words[i]:
				words_with_x.append(i)
		return words_with_x


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.findWordsContaining


BaseSolutionTest(TestableSolution, )
