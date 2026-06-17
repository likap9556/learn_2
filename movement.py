
class LinearMovement:
    def __init__(self, obj, dt: float = 1.0):
        self.obj = obj
        self.dt = dt
    
    def move(self):
        if not hasattr(self.obj, "position"):
            raise AttributeError("Нет доступа к position")

        if not hasattr(self.obj, "velocity"):
            raise AttributeError("Нет доступа к velocity")

        self.obj.position = self.obj.position + self.obj.velocity * self.dt