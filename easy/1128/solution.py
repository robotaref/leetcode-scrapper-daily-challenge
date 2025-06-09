from testing.solution_test import BaseSolutionTest
from typing import List

def check_equivalent(domino_1: List[int], domino_2: List[int]) -> bool:
	if (domino_1[0] == domino_2[0] and domino_1[1] == domino_2[1]) or (domino_1[0] == domino_2[1] and domino_1[1] == domino_2[0]):
		return True
	else:
		return False

def domino2str(domino: List[int]):
	return str(min(domino[0], domino[1])) + "_" + str(max(domino[0], domino[1]))


class Solution:
	def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
		count = 0
		seen = {domino2str(dominoes[0]): [dominoes[0]]}

		for d in dominoes[1:]:
			if domino2str(d) in seen.keys():
				count += len(seen[domino2str(d)])
				seen[domino2str(d)].append(d)
			else:
				seen[domino2str(d)] = [d]

		return count

class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.numEquivDominoPairs


BaseSolutionTest(TestableSolution, )
