from geometry import Vector
from abc import ABC, abstractmethod
from geometry import Vector


class PositionReadable(ABC):
    @property
    @abstractmethod
    def position(self):
        pass


class PositionWritable(ABC):
    @property
    @abstractmethod
    def position(self):
        pass

    @position.setter
    @abstractmethod
    def position(self, value):
        pass


class VelocityReadable(ABC):
    @property
    @abstractmethod
    def velocity(self):
        pass


class Rotatable(ABC):
    @abstractmethod
    def direction(self):
        pass

    @abstractmethod
    def rotate(self, angle: float):
        pass


class SpaceObject(PositionReadable, PositionWritable, VelocityReadable):
    def __init__(self, position: Vector, velocity: Vector):
        self._position = position
        self._velocity = velocity

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def velocity(self):
        return self._velocity
    

class Ship(SpaceObject, Rotatable):
    def __init__(self, position: Vector, velocity: Vector):
        super().__init__(position, velocity)
        self._direction = Vector(0, 1)

    @property
    def direction(self):
        return self._direction

    def rotate(self, angle: float):
        self._direction = self._direction.rotate(angle)