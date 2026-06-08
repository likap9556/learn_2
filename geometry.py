import math
from dataclasses import dataclass


@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k: float):
        return Vector(self.x * k, self.y * k)

    def rotate(self, angle: float):
        rad = math.radians(angle)
        return Vector(
            self.x * math.cos(rad) - self.y * math.sin(rad),
            self.x * math.sin(rad) + self.y * math.cos(rad),
        )