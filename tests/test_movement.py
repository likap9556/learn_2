from objects import SpaceObject
from geometry import Vector
from movement import LinearMovement


def test_linear_movement():
    obj = SpaceObject(Vector(12, 5), Vector(-7, 3))
    mover = LinearMovement(obj, 1)

    mover.move()

    assert obj.position.x == 5
    assert obj.position.y == 8