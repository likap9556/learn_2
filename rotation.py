from objects import Rotatable


class RotationSystem:
    def rotate(self, obj: Rotatable, angle: float):
        if not hasattr(obj, "rotate"):
            raise AttributeError("Объект не поддерживает вращение")

        obj.rotate(angle)