from command import Command

class LogCommand(Command):
    def __init__(self, cmd, exc):
        self.cmd = cmd
        self.exc = exc

    def execute(self):
        print(f"ERROR: {type(self.cmd).__name__}: {self.exc}")

class RetryOnceCommand(Command):
    def __init__(self, cmd):
        self.cmd = cmd 

    def execute(self):
        self.cmd.execute()

class RetryTwiceCommand(Command):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()
