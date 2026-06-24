from infrastructure.command_queue import CommandQueue
from infrastructure.command_processor import CommandProcessor
from infrastructure.exception_handler_registry import ExceptionHandlerRegistry

from handlers.retry_once_handler import RetryOnceHandler
from handlers.retry_once_failed_handler import RetryOnceFailedHandler
from handlers.retry_twice_failed_handler import RetryTwiceFailedHandler

from commands.move_command import MoveCommand
from commands.retry_once_command import RetryOnceCommand
from commands.retry_twice_command import RetryTwiceCommand


queue = CommandQueue()
registry = ExceptionHandlerRegistry()

registry.register(MoveCommand, RuntimeError, RetryOnceHandler())
registry.register(RetryOnceCommand, RuntimeError, RetryOnceFailedHandler())
registry.register(RetryTwiceCommand, RuntimeError, RetryTwiceFailedHandler())

queue.push(MoveCommand("obj"))

processor = CommandProcessor(queue, registry)
processor.process()