from testing.solution_test import BaseSolutionTest
from typing import List


def bfs(start: int, edges: List[int]) -> List[int]:
	distance = [-1] * (len(edges))
	distance[start] = 0

	node = start
	dead_end = False
	while not dead_end:
		if edges[node] == -1:
			break
		if distance[edges[node]] == -1:
			distance[edges[node]] = distance[node] + 1
		else:
			break
		node = edges[node]

	return distance


class Solution:
	def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
		distances_1 = bfs(node1, edges)
		distances_2 = bfs(node2, edges)

		minimum_distance = len(edges)
		winner = -1
		for i in range(len(edges)):
			if distances_1[i] >= 0 and distances_2[i] >= 0:
				if minimum_distance > max(distances_1[i], distances_2[i]):
					minimum_distance = max(distances_1[i], distances_2[i])
					winner = i

		return winner


class TestableSolution(Solution):
	def __init__(self):
		super().__init__()
		self.main = self.closestMeetingNode


BaseSolutionTest(TestableSolution, )
