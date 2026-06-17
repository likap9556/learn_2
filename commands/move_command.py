from command import Command
from movement import LinearMovement

class MoveCommand(Command):

    def __init__(self, obj):
        self.obj = obj

    def execute(self):
        LinearMovement(self.obj).move()