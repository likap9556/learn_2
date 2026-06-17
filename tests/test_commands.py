from tests.failig_object import FailingObject

from commands.move_command import MoveCommand
from commands.retry_once_command import RetryOnceCommand
from commands.retry_twice_command import RetryTwiceCommand

from handlers.retry_once_handler import RetryOnceHandler
from handlers.retry_once_failed_handler import RetryOnceFailedHandler
from handlers.retry_twice_failed_handler import RetryTwiceFailedHandler

from infrastructure.command_queue import CommandQueue
from infrastructure.command_processor import CommandProcessor
from infrastructure.handler_registry import ExceptionHandlerRegistry

def test_retry_twice_then_log():
    obj = FailingObject()

    queue = CommandQueue()
    queue.push(MoveCommand(obj))

    registry = ExceptionHandlerRegistry()

    registry.register(
        MoveCommand,
        AttributeError,
        RetryOnceHandler()
    )

    registry.register(
        RetryOnceCommand,
        AttributeError,
        RetryOnceFailedHandler()
    )

    registry.register(
        RetryTwiceCommand,
        AttributeError,
        RetryTwiceFailedHandler()
    )

    processor = CommandProcessor(queue, registry)
    processor.process()

    assert queue.empty()

def test_log_command_created():
    obj = FailingObject()

    queue = CommandQueue()
    queue.push(MoveCommand(obj))

    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, AttributeError, RetryOnceHandler())
    registry.register(RetryOnceCommand, AttributeError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, AttributeError, RetryTwiceFailedHandler())

    processor = CommandProcessor(queue, registry)
    processor.process()

    assert queue.empty()

def test_two_retry_attempts():
    obj = FailingObject()

    queue = CommandQueue()
    queue.push(MoveCommand(obj))

    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, AttributeError, RetryOnceHandler())
    registry.register(RetryOnceCommand, AttributeError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, AttributeError, RetryTwiceFailedHandler())

    processor = CommandProcessor(queue, registry)
    processor.process()
    assert obj.calls == 3

def test_retry_creates_new_command():
    obj = FailingObject()

    queue = CommandQueue()
    queue.push(MoveCommand(obj))

    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, AttributeError, RetryOnceHandler())

    processor = CommandProcessor(queue, registry)
    processor.process()
    assert queue.empty()


def test_log_output(capsys):
    obj = FailingObject()

    queue = CommandQueue()
    queue.push(MoveCommand(obj))

    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, AttributeError, RetryOnceHandler())
    registry.register(RetryOnceCommand, AttributeError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, AttributeError, RetryTwiceFailedHandler())

    processor = CommandProcessor(queue, registry)
    processor.process()

    captured = capsys.readouterr()

    assert "LOG" in captured.out or "RetryTwiceCommand" in captured.out