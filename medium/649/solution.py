import collections

from testing.solution_test import BaseSolutionTest


class Solution:
    opponent = {}
    answers = {"R": "Radiant", "D": "Dire"}

    @staticmethod
    def game_still_on(senate):
        if len(senate) == 1:
            return False
        elif senate.count("R") == 0 or senate.count("D") == 0:
            return False
        return True

    def war(self, senate):
        i = senate.find(self.opponent[senate[0]])
        senate = senate[:i] + senate[i + 1:]
        senate = senate[1:] + senate[0]
        return senate

    def predictPartyVictory(self, senate: str) -> str:
        self.opponent = {"R": "D", "D": "R"}
        while self.game_still_on(senate):
            senate = self.war(senate)
        return self.answers[senate[0]]

    @staticmethod
    def predictPartyVictoryV2(senate):

        n = len(senate)
        qr = collections.deque([i for i, c in enumerate(senate) if c == "R"])
        qd = collections.deque([i for i, c in enumerate(senate) if c == "D"])
        while qr and qd:
            if qr[0] < qd[0]:
                qd.popleft()
                qr.append(qr.popleft() + n)
            else:
                qr.popleft()
                qd.append(qd.popleft() + n)
        return "Radiant" if qr else "Dire"


class TestableSolution(Solution):
    def __init__(self):
        super().__init__()
        self.main = self.predictPartyVictoryV2


BaseSolutionTest(TestableSolution)
