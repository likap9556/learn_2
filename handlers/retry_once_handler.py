from handlers.exception_handler import ExceptionHandler
from commands.retry_once_command import RetryOnceCommand


class RetryOnceHandler(ExceptionHandler):

    def handle(self, cmd, exc):
        return RetryOnceCommand(cmd)