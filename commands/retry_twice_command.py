from command import Command


class RetryTwiceCommand(Command):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()