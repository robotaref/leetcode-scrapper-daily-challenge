from testing.solution_test import BaseSolutionTest
from typing import List
from collections import deque, defaultdict

import numpy as np


def compute_tree_distances(edges_list: List[List[int]]) -> np.array:
	adj = defaultdict(list)
	for u, v in sorted(edges_list):
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
					if distance[node] == 0:
						distance[neighbor] = 1
						queue.append(neighbor)
					else:
						distance[neighbor] = 0
						queue.append(neighbor)
		return distance

	return bfs(edges_list[0][0])


class Solution:
	def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
		distances_1 = compute_tree_distances(edges1)
		distances_2 = compute_tree_distances(edges2)

		odds1 = sum(distances_1)
		odds2 = max(sum(distances_2), len(edges2) + 1 - sum(distances_2))

		evens1 = len(edges1) - odds1 + 1

		answer = [0] * (len(edges1) + 1)
		for i in range(len(edges1) + 1):
			if distances_1[i] == 0:
				answer[i] = evens1 + odds2
			else:
				answer[i] = odds1 + odds2

		return answer


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.maxTargetNodes


BaseSolutionTest(TestableSolution, )
