from math import sqrt, pow


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __mul__(self, s):
        x = self.x * s
        y = self.y * s
        return Point(x, y)


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.magnitutde = sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __init__(self, a: Point, b: Point):
        self.x = b.x - a.x
        self.y = b.y - a.y
        self.magnitutde = sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, s):
        x = self.x * s
        y = self.y * s
        return Vector(x, y)

    def normalized(self):
        return Vector(self.x / self.magnitutde, self.y / self.magnitutde)

    def mean_point(self, a: Point, b: Point):
        return Point((a.x + b.x) / 2.0, (a.y + b.y) / 2.0)
