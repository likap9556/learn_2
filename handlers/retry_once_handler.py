from commands.retry_once_command import RetryOnceCommand
from handlers.exception_handler import ExceptionHandler


class RetryOnceHandler(ExceptionHandler):
    def handle(self, cmd, exc, queue):
        queue.push(RetryOnceCommand(cmd))