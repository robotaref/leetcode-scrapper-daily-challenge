from testing.solution_test import BaseSolutionTest


class Solution:
    def pivotInteger(self, n: int) -> int:
        s = sum(range(n + 1))
        p = 0
        for i in range(1, n + 1):
            p += i
            if p == s - p + i:
                return i
        return -1


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.pivotInteger


BaseSolutionTest(TestableSolution, )
