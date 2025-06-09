from testing.solution_test import BaseSolutionTest


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		max_length = len(s)
		current_length = len(set(s))

		found = False

		while not found:
			counter = 0
			while current_length + counter <= max_length:
				sub = s[counter:current_length + counter]
				if len(set(sub)) == len(sub):
					found = True
					break
				else:
					counter += 1
			if found:
				break
			else:
				current_length -= 1

		return current_length


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.lengthOfLongestSubstring


BaseSolutionTest(TestableSolution, )
