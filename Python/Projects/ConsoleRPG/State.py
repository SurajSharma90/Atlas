from enum import Enum

class StateTypes(Enum):
    MAIN_MENU = 0
    GAME = 1

class State:
    def __init__(self, type):
        self.type = type

    def update(self):
        print(self.type)
