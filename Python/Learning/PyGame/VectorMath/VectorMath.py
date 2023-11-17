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

    """
    def __add__(self, other):
        return Vectorf(Vector2f(self.x + other.x), self.y + other.y)
    """

    def normalized(self):
        return Vectorf(self.x / self.magnitutde, self.y / self.magnitutde)
    
    def mean_point(self, a:Vector2f, b:Vector2f):
        return Vector2f((a.x + b.x)/2.0, (a.y + b.y)/2.0)
