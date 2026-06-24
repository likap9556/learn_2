from commands.move_command import MoveCommand

class FailingMoveCommand(MoveCommand):

    def __init__(self, obj):
        super().__init__(obj)
        self.calls = 0

    def execute(self):
        self.calls += 1
        print(f"execute attempt {self.calls}")
        raise RuntimeError("boom")