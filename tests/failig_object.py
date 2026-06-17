from geometry import Vector

class FailingObject:
    def __init__(self):
        self.calls = 0

    @property
    def position(self):
        self.calls += 1
        raise AttributeError("fail")

    @position.setter
    def position(self, value):
        pass

    @property
    def velocity(self):
        return Vector(1, 1)