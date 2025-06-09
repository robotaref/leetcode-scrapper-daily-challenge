from testing.solution_test import BaseSolutionTest
from typing import List

import numpy as np


class Solution:
	def longestPalindrome(self, words: List[str]) -> int:
		current_length = 0
		words = np.array(words)

		mid_element = False

		while len(words) > 0:
			word = words[0]
			b_word = word[::-1]

			indices = np.where(words == word)
			b_indices = np.where(words == b_word)

			len_index = len(indices[0])
			len_bindex = len(b_indices[0])

			if len_bindex != 0:

				if len_index >= len_bindex:
					occurrences = len_bindex
					words = np.delete(words, np.concatenate([b_indices[0], indices[0][:occurrences]]))

				else:
					occurrences = len_index
					words = np.delete(words, np.concatenate([indices[0], b_indices[0][:occurrences]]))
				if word != b_word:
					current_length += occurrences * 4
				elif len_index % 2 == 0:
					current_length += occurrences * 2
				elif not mid_element:
					current_length += occurrences * 2
					mid_element = True
				else:
					current_length += occurrences * 2 - 2

			elif not mid_element and b_word == word:
				mid_element = True
				current_length += 2
				words = np.delete(words, 0)
			else:
				words = np.delete(words, indices)

		return current_length


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.longestPalindrome


BaseSolutionTest(TestableSolution, )
