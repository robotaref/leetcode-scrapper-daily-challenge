import bisect
from collections import defaultdict
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit), key=lambda x: x[0], reverse=False)
        worker = sorted(worker, reverse=True)
        sorted_diff = [job[0] for job in jobs]
        sorted_profit = [job[1] for job in jobs]
        s = 0
        s_w = defaultdict(lambda: 0)
        for w in worker:
            i = bisect.bisect_right(sorted_diff, w)
            sorted_profit = sorted_profit[:i]
            if w not in s_w.keys():
                s_w[w] = max(sorted_profit) if len(sorted_profit) > 0 else 0
            s += s_w[w]
        return s


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.maxProfitAssignment


BaseSolutionTest(TestableSolution, )
