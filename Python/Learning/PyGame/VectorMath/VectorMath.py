from math import sqrt, pow


class Vector2f:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Vectorf:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.magnitutde = sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __init__(self, a: Vector2f, b: Vector2f):
        self.x = b.x - a.x
        self.y = b.y - a.y
        self.magnitutde = sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normalize():
        return self.__init__()
