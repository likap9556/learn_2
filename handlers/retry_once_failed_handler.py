from handlers.exception_handler import ExceptionHandler
from commands.retry_twice_command import RetryTwiceCommand


class RetryOnceFailedHandler(ExceptionHandler):

    def handle(self, cmd, exc):
        return RetryTwiceCommand(cmd.cmd)