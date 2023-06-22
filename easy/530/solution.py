from typing import Optional

from testing.solution_test import BaseSolutionTest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.getMinimumDifference


BaseSolutionTest(TestableSolution, )
