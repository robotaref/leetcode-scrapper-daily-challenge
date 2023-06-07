from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.main = self.minFlips

    def minFlips(self, a: int, b: int, c: int) -> int:
        n = 0
        while a != 0 or b != 0 or c != 0:
            a_last = a & 1
            b_last = b & 1
            c_last = c & 1
            if c_last & (~ (a_last | b_last)):
                n += 1
            elif ~ c_last & (a_last & b_last):
                n += 2
            elif ~ c_last & ~ (a_last & b_last) & (a_last | b_last):
                n += 1

            a = a >> 1
            b = b >> 1
            c = c >> 1
        return n


BaseSolutionTest(Solution, )
