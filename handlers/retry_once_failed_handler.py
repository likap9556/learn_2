from commands.retry_twice_command import RetryTwiceCommand
from handlers.exception_handler import ExceptionHandler


class RetryOnceFailedHandler(ExceptionHandler):
    def handle(self, cmd, exc, queue):
        queue.push(RetryTwiceCommand(cmd))