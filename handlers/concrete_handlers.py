from handlers.exception_handler import ExceptionHandler
from commands.retry_commands import RetryOnceCommand, RetryTwiceCommand, LogCommand

class RetryOnceHandler(ExceptionHandler):
    def handle(self, cmd, exc):
        # cmd — это MoveCommand. Оборачиваем её в первый повтор.
        return RetryOnceCommand(cmd)

class RetryOnceFailedHandler(ExceptionHandler):
    def handle(self, cmd, exc):
        # cmd — это упавшая RetryOnceCommand. 
        # Достаем оригинальную команду через cmd.cmd и оборачиваем во второй повтор.
        return RetryTwiceCommand(cmd.cmd)

class RetryTwiceFailedHandler(ExceptionHandler):
    def handle(self, cmd, exc):
        # cmd — это упавшая RetryTwiceCommand.
        # Достаем оригинальную команду и отправляем в лог.
        return LogCommand(cmd.cmd, exc)
