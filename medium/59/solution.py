from typing import List

from base_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.main = self.generateMatrix

    def generateMatrix(self, n: int) -> List[List[int]]:
        up = 1
        right = 1
        x = 0
        y = 0
        num = 1
        x_limit = n
        y_limit = n
        x_lower = 0
        y_lower = 1
        matrix = [[0 for i in range(n)] for j in range(n)]
        while num < n * n + 1:
            while x_limit > x >= x_lower:
                matrix[y][x] = num
                num += 1
                x += right
            if right == 1:
                x_limit -= 1
            else:
                x_lower += 1
            right = -right
            x += right
            y += up
            while y_limit > y >= y_lower:
                matrix[y][x] = num
                num += 1
                y += up
            if up == 1:
                y_limit -= 1
            else:
                y_lower += 1

            up = -up
            x += right
            y += up
        return matrix


BaseSolutionTest(Solution(), used_tests=[1])
