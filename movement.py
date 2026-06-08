
class LinearMovement:
    def move(self, obj, dt: float = 1.0):
        if not hasattr(obj, "position"):
            raise AttributeError("Нет доступа к position")

        if not hasattr(obj, "velocity"):
            raise AttributeError("Нет доступа к velocity")

        obj.position = obj.position + obj.velocity * dt