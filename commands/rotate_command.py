from command import Command
from rotation import RotationSystem

class RotateCommand(Command):

    def __init__(self, obj, angle):
        self.obj = obj
        self.angle = angle

    def execute(self):
        RotationSystem().rotate(self.obj, self.angle)