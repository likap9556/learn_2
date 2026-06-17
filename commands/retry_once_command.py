from command import Command


class RetryOnceCommand(Command):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()