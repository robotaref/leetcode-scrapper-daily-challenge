from typing import List
from testing.solution_test import BaseSolutionTest


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
		if n == 0:
			pass
		elif m == 0:
			nums1 = nums2
		else:
			i = 0
			j = 0
			while i < m+j and j < n:
				if nums1[i] <= nums2[j]:
					i += 1
				else:
					nums1[i + 1: m + 1 + j] = nums1[i: m + j]
					nums1[i] = nums2[j]
					i += 1
					j += 1
			nums1[i:] = nums2[j:]
		return nums1


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.merge


BaseSolutionTest(TestableSolution, )
