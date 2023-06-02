from collections import deque
from typing import Optional

from solution_test import BaseSolutionTest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.main = self.pairSum

    def pairSum(self, head: Optional[ListNode]) -> int:
        q = deque()
        used = head
        while used is not None:
            q.append(used.val)
            q.appendleft(used.val)
            used = used.next
        m = 0
        s = 0
        n = len(q) // 2
        for i in range(n):
            s = q[i] + q[i + n]
            if s > m:
                m = s
        return m


BaseSolutionTest(Solution())
