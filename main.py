from infrastructure.command_queue import CommandQueue
from infrastructure.command_processor import CommandProcessor
from infrastructure.exception_handler_registry import ExceptionHandlerRegistry

from handlers.concrete_handlers import RetryOnceHandler, RetryOnceFailedHandler, RetryTwiceFailedHandler

from commands.move_command import MoveCommand
from commands.retry_commands import RetryOnceCommand, RetryTwiceCommand


queue = CommandQueue()
registry = ExceptionHandlerRegistry()

# MoveCommand - RetryOnceHandler
registry.register(MoveCommand, ValueError, RetryOnceHandler())

# RetryOnceCommand -RetryOnceFailedHandler
registry.register(RetryOnceCommand, ValueError, RetryOnceFailedHandler())

# RetryTwiceCommand - RetryTwiceFailedHandler
registry.register(RetryTwiceCommand, ValueError, RetryTwiceFailedHandler())

# неработающая команда
queue.push(MoveCommand(obj="ship"))

processor = CommandProcessor(queue, registry)
print("start")
processor.process()
print("end")
