import pytest

from commands.retry_once_command import RetryOnceCommand
from commands.retry_twice_command import RetryTwiceCommand
from failing_object import FailingMoveCommand

from infrastructure.command_queue import CommandQueue
from infrastructure.command_processor import CommandProcessor
from infrastructure.exception_handler_registry import ExceptionHandlerRegistry

from handlers.retry_once_handler import RetryOnceHandler
from handlers.retry_once_failed_handler import RetryOnceFailedHandler
from handlers.retry_twice_failed_handler import RetryTwiceFailedHandler

from commands.move_command import MoveCommand



def test_execution_order():

    queue = CommandQueue()
    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, RuntimeError, RetryOnceHandler())
    registry.register(MoveCommand, RuntimeError, RetryOnceHandler())
    registry.register(RetryOnceCommand, RuntimeError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, RuntimeError, RetryTwiceFailedHandler())

    cmd = FailingMoveCommand("obj")
    queue.push(cmd)

    processor = CommandProcessor(queue, registry)
    processor.process()

    assert cmd.calls == 3
    assert queue.empty()


def test_log_output(capsys):

    queue = CommandQueue()
    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, RuntimeError, RetryOnceHandler())
    registry.register(RetryOnceCommand, RuntimeError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, RuntimeError, RetryTwiceFailedHandler())

    queue.push(FailingMoveCommand("obj"))

    processor = CommandProcessor(queue, registry)
    processor.process()

    captured = capsys.readouterr().out

    assert "ERROR" in captured
    assert "FailingMoveCommand" in captured


def test_retry_depth():

    queue = CommandQueue()
    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, RuntimeError, RetryOnceHandler())
    registry.register(RetryOnceCommand, RuntimeError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, RuntimeError, RetryTwiceFailedHandler())

    queue.push(FailingMoveCommand("obj"))

    processor = CommandProcessor(queue, registry)
    processor.process()

    assert queue.empty()


def test_no_infinite_loop():

    queue = CommandQueue()
    registry = ExceptionHandlerRegistry()

    registry.register(MoveCommand, RuntimeError, RetryOnceHandler())
    registry.register(RetryOnceCommand, RuntimeError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, RuntimeError, RetryTwiceFailedHandler())

    queue.push(FailingMoveCommand("obj"))

    processor = CommandProcessor(queue, registry)

    processor.process()

    assert queue.empty()