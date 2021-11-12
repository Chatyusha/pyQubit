import math


class vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(x**2+y**2)
