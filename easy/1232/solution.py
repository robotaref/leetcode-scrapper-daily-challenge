from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.main = self.checkStraightLine

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        m = None
        for i, (x, y) in enumerate(coordinates[1:]):
            if x0 != x:
                if m is None:
                    if i > 0:
                        return False
                    m = (y - y0) / (x - x0)
                else:
                    if m != (y - y0) / (x - x0):
                        return False

            else:
                if m is not None:
                    return False

        return True


BaseSolutionTest(Solution, )
