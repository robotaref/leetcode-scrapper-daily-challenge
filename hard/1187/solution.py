import bisect
from typing import List

from testing.solution_test import BaseSolutionTest


class Solution:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
        self.n = 0
        self.m = 0

    def make(self, i):
        print(i, self.arr1[:i], self.arr2)
        if i == self.n:
            return 0
        if self.arr1[i] > self.arr1[i - 1]:
            k = bisect.bisect_right(self.arr2, self.arr1[i - 1])
            self.arr2 = self.arr2[k:]
            return self.make(i + 1)
        else:
            if len(self.arr2) == 0:
                return -1
            self.arr1[i - 1] = self.arr2[0]
            self.arr2 = self.arr2[1:]
            k = 1
            if self.arr1[i - 1] >= self.arr1[i]:
                if len(self.arr2) == 0:
                    return -1
                self.arr1[i] = self.arr2[0]
                self.arr2 = self.arr2[1:]
                k = 2
            c = self.make(i + 1)
            if c == -1:
                return -1
            return c + k

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        self.n = len(arr1)
        self.m = len(arr2)
        arr2.sort()
        print(arr2)
        self.arr1 = arr1
        self.arr2 = arr2
        return self.make(1)


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.makeArrayIncreasing


BaseSolutionTest(TestableSolution, used_tests=[3])
