from handlers.exception_handler import ExceptionHandler
from commands.log_command import LogCommand


class RetryTwiceFailedHandler(ExceptionHandler):

    def handle(self, cmd, exc):
        return LogCommand(cmd.cmd, exc)