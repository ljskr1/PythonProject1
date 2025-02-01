import math

from vector import Vector

class Vector3D(Vector):
    def __init__(self, x, y, z):
        Vector.__init__(self, x, y)
        self._z = z

    def magnitude(self): #method over-riding
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)

    def __str__(self):
        return f"{self._x}, {self._y}, {self._z} | Magnitude:{round(self.magnitude(),2)}"

if __name__ == "__main__":
    v = Vector3D(1, 2, 3)
    v1 = Vector(1, 2)
    print("3D:",v)
    print("2D:",v1)

