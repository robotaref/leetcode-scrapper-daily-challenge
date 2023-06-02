class MyHashSet:

    def __init__(self):
        self.m = 1000
        self.table = [[] for _ in range(self.m)]

    def add(self, key: int) -> None:
        spot = key % self.m
        if not self.contains(key):
            self.table[spot].append(key)

    def remove(self, key: int) -> None:
        spot = key % self.m
        if self.contains(key):
            i = self.table[spot].index(key)
            self.table[spot].pop(i)

    def contains(self, key: int) -> bool:
        spot = key % self.m
        return key in self.table[spot]


BaseSolutionTest(Solution)
