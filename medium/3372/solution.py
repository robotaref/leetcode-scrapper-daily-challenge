from testing.solution_test import BaseSolutionTest
from typing import List
from collections import deque, defaultdict


import numpy as np


def compute_tree_distances(edges_list: List[List[int]]) -> np.array:
	adj = defaultdict(list)
	for u, v in edges_list:
		adj[u].append(v)
		adj[v].append(u)

	def bfs(start: int) -> List[int]:
		distance = [-1] * (len(edges_list)+1)
		queue = deque([start])
		distance[start] = 0
		while queue:
			node = queue.popleft()
			for neighbor in adj[node]:
				if distance[neighbor] == -1:
					distance[neighbor] = distance[node] + 1
					queue.append(neighbor)
		return distance

	distance_matrix = [0] * (len(edges_list)+1)
	for v in range(len(edges_list) + 1):
		distance_matrix[v] = bfs(v)

	return np.array(distance_matrix)


class Solution:
	def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
		distances_1 = compute_tree_distances(edges1)
		distances_2 = compute_tree_distances(edges2)

		sums_1 = [0] * (len(edges1) + 1)
		sums_2 = [0] * (len(edges2) + 1)

		for i in range(len(distances_1)):
			sums_1[i] = len(np.where(distances_1[i] <= k)[0])

		for i in range(len(distances_2)):
			sums_2[i] = len(np.where(distances_2[i] <= k - 1)[0])

		m = max(sums_2)

		sums = [s + m for s in sums_1]

		return sums


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.maxTargetNodes


BaseSolutionTest(TestableSolution, )
