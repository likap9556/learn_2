import pytest
from movement import LinearMovement
from geometry import Vector

def test_no_position():
    class Bad:
        @property
        def velocity(self):
            return Vector(1, 1)

    with pytest.raises(AttributeError):
        LinearMovement().move(Bad(), 1)


def test_no_velocity():
    class Bad:
        @property
        def position(self):
            return Vector(0, 0)

        @position.setter
        def position(self, value):
            pass

    with pytest.raises(AttributeError):
        LinearMovement().move(Bad(), 1)