from solution_test import BaseSolutionTest


class Solution:

    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.main = self.maxVowels

    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k

        cnt = self.count_in(s, left, right)
        last_substring_cnt = cnt
        while right < len(s) and cnt != k:
            if s[left] in self.vowels:
                last_substring_cnt -= 1
            if s[right] in self.vowels:
                last_substring_cnt += 1
            cnt = max(cnt, last_substring_cnt, )
            right += 1
            left += 1
        return cnt

    def count_in(self, s, left, right):
        cnt = 0
        for c in s[left:right]:
            if c in self.vowels:
                cnt += 1
        return cnt


BaseSolutionTest(Solution())
