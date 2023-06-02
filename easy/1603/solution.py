from command_test import BaseCommandTest


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.space[carType] <= 0:
            return False
        else:
            self.space[carType] -= 1
            return True


BaseCommandTest(ParkingSystem)
