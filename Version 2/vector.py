from os import stat


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = (x, y)
        self.magnitude =  ((x ** 2) + (y ** 2)) ** 0.5

    @staticmethod
    def Add(v1, v2):
        return Vector(v1.x + v2.x, v1.y + v2.y)

    @staticmethod
    def Subtract(v1, v2):
        return Vector(v1.x - v2.x, v1.y - v2.y)

    @staticmethod
    def Dot(v1, v2):
        return sum([i[0] * i[1] for i in zip(v1.vector, v2.vector)])