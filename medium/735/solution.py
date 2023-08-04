from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = []
        left = []
        for ast in asteroids:
            if ast < 0:
                left.append(ast)
            else:
                right.append(ast)
            while right and left:
                r = right.pop()
                l = abs(left.pop())
                if r > l:
                    right.append(r)
                elif l > r:
                    left.append(-l)
        if right:
            return right
        else:
            return left


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.asteroidCollision


BaseSolutionTest(TestableSolution, )
