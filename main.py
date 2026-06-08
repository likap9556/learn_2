import math
from abc import ABC, abstractmethod
from dataclasses import dataclass

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
    

class LinearMovement:
    def move(self, obj: SpaceObject, dt: float = 1.0):
        if not hasattr(obj, "position"):
            raise AttributeError("Нет доступа к position")

        if not hasattr(obj, "velocity"):
            raise AttributeError("Нет доступа к velocity")

        if not hasattr(obj, "position") or not hasattr(obj, "__setattr__"):
            raise AttributeError("Невозможно изменить position")

        obj.position = obj.position + obj.velocity * dt


class RotationSystem:
    def rotate(self, obj: Rotatable, angle: float):
        if not hasattr(obj, "rotate"):
            raise AttributeError("Объект не поддерживает вращение")

        obj.rotate(angle)

class Ship(SpaceObject, Rotatable):
    def __init__(self, position: Vector, velocity: Vector):
        super().__init__(position, velocity)
        self._direction = Vector(0, 1)

    @property
    def direction(self):
        return self._direction

    def rotate(self, angle: float):
        self._direction = self._direction.rotate(angle)


def test_linear_movement():
    obj = SpaceObject(Vector(12, 5), Vector(-7, 3))
    mover = LinearMovement()

    mover.move(obj, dt=1)

    assert obj.position.x == 5
    assert obj.position.y == 8

def test_no_position():
    class BadObj:
        @property
        def velocity(self):
            return Vector(1, 1)

    mover = LinearMovement()

    try:
        mover.move(BadObj(), 1)
        assert False
    except AttributeError:
        assert True

def test_no_velocity():
    class BadObj:
        @property
        def position(self):
            return Vector(0, 0)

        @position.setter
        def position(self, value):
            pass

    mover = LinearMovement()

    try:
        mover.move(BadObj(), 1)
        assert False
    except AttributeError:
        assert True

def test_cannot_set_position():
    class BadObj:
        @property
        def position(self):
            return Vector(0, 0)

        @property
        def velocity(self):
            return Vector(1, 1)

    mover = LinearMovement()

    try:
        mover.move(BadObj(), 1)
        assert False
    except AttributeError:
        assert True

def test_rotation():
    ship = Ship(Vector(0, 0), Vector(0, 0))
    rotator = RotationSystem()

    rotator.rotate(ship, 90)

    assert round(ship.direction.x, 5) == 0
    assert round(ship.direction.y, 5) == 1