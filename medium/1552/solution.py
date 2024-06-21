import bisect
from typing import List

from testing.solution_test import BaseSolutionTest

class Solution:
    def is_possible(self, position, m, d):
        # print(d)
        prev_ball_pos = position[0]
        balls_placed = 1

        # Iterate on each 'position' and place a ball there if we can place it.
        for i in range(1, len(position)):
            curr_pos = position[i]
            # Check if we can place the ball at the current position.
            if curr_pos - prev_ball_pos >= d:
                balls_placed += 1
                prev_ball_pos = curr_pos
            # If all 'm' balls are placed, return 'True'.
            if balls_placed == m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        max_l = (max(position) - min(position)) // (m - 1)
        min_l = 1
        ok_times = []
        c = 0
        while max_l > min_l + 1:
            c += 1
            d = (max_l + min_l) // 2
            # print("min max", min_l, max_l, d)

            if self.is_possible(position, m, d):
                min_l = (min_l + max_l) // 2
                ok_times.append(d)
            else:
                max_l = (min_l + max_l) // 2
            if max_l == min_l:
                return max_l
        return max_l if self.is_possible(position, m, max_l) else min_l


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.maxDistance


BaseSolutionTest(TestableSolution, )
