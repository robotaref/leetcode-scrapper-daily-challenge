import collections
from typing import List

from base_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.spiralOrder

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        up = 1
        right = 1
        x = 0
        y = 0
        answer = []
        x_limit = n
        y_limit = m
        x_lower = 0
        y_lower = 1
        while len(answer) < n * m:
            while x_limit > x >= x_lower:
                answer.append(matrix[y][x])
                x += right

            if right == 1:
                x_limit -= 1
            else:
                x_lower += 1
            right = -right
            x += right
            y += up
            while y_limit > y >= y_lower:
                answer.append(matrix[y][x])
                y += up
            if up == 1:
                y_limit -= 1
            else:
                y_lower += 1
            up = -up
            x += right
            y += up
        return answer


BaseSolutionTest(Solution())
