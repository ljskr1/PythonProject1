#polymorphism is the porcess in the which different functions different outputs through __ __ magic funcitons
import math
"""
global functions
class definition
main

"""

#create a vector class
class Vector:
    def __init__(self, x = 0, y =0):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __len__(self):
        return int(self.magnitude())

    def __str__(self):
        return f'({self.x}, {self.y}) | Magnitue: {round(self.magnitude(), 2)}'

    def __repr__(self):
        return f'({self.x}, {self.y}) | Class: "Vector"'

if __name__ == "__main__":
    v = Vector(1, 2)
    print(v)