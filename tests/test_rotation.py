from geometry import Vector
from rotation import RotationSystem
from objects import Ship


def test_rotation():
    ship = Ship(Vector(0, 0), Vector(0, 0))
    rotator = RotationSystem()

    rotator.rotate(ship, 90)

    assert round(ship.direction.x, 5) == -1
    assert round(ship.direction.y, 5) == 0