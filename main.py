from geometry import Vector
from objects import SpaceObject

from commands.move_command import MoveCommand
from commands.retry_once_command import RetryOnceCommand
from commands.retry_twice_command import RetryTwiceCommand

from handlers.retry_once_handler import RetryOnceHandler
from handlers.retry_once_failed_handler import RetryOnceFailedHandler
from handlers.retry_twice_failed_handler import RetryTwiceFailedHandler

from infrastructure.command_queue import CommandQueue
from infrastructure.command_processor import CommandProcessor
from infrastructure.handler_registry import ExceptionHandlerRegistry


obj = SpaceObject(None, Vector(1, 1))

queue = CommandQueue()
queue.push(MoveCommand(obj))

registry = ExceptionHandlerRegistry()

registry.register(MoveCommand, AttributeError, RetryOnceHandler())
registry.register(RetryOnceCommand, AttributeError, RetryOnceFailedHandler())
registry.register(RetryTwiceCommand, AttributeError, RetryTwiceFailedHandler())

processor = CommandProcessor(queue, registry)
processor.process()