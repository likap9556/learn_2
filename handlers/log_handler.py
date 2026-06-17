from commands.log_command import LogCommand
from handlers.exception_handler import ExceptionHandler

class LogHandler(ExceptionHandler):

    def handle(self, cmd, exc, queue):
        queue.push(LogCommand(cmd, exc))