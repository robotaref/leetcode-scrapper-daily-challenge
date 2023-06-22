from testing.command_test import BaseCommandTest


class SnapshotArray:

    def __init__(self, length: int):
        self.logs = []
        self.snaps = []
        self.n = length

    def set(self, index: int, val: int) -> None:
        self.logs.append([index, val])

    def snap(self) -> int:
        self.snaps.append(len(self.logs))
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        for i in range(self.snaps[snap_id] - 1, -1, -1):
            if self.logs[i][0] == index:
                return self.logs[i][1]
        return 0


BaseCommandTest(SnapshotArray, )
