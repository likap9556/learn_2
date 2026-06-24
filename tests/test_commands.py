import pytest
from unittest.mock import Mock

from command import Command
from infrastructure.command_queue import CommandQueue
from infrastructure.exception_handler_registry import ExceptionHandlerRegistry
from infrastructure.command_processor import CommandProcessor
from commands.retry_commands import RetryOnceCommand, RetryTwiceCommand
from commands.move_command import MoveCommand
from handlers.concrete_handlers import RetryOnceHandler, RetryOnceFailedHandler, RetryTwiceFailedHandler

class BrokenMoveCommand(MoveCommand):
    def execute(self):
        raise ValueError("ошибка")

# повтор 2 раза - запись в лог
def test_double_retry_then_log_scenario(capsys):
    queue = CommandQueue()
    registry = ExceptionHandlerRegistry()
    
    registry.register(BrokenMoveCommand, ValueError, RetryOnceHandler())
    registry.register(RetryOnceCommand, ValueError, RetryOnceFailedHandler())
    registry.register(RetryTwiceCommand, ValueError, RetryTwiceFailedHandler())
    
    bad_move = BrokenMoveCommand(obj="ship")
    queue.push(bad_move)
    
    processor = CommandProcessor(queue, registry)
    processor.process()
    
    # вывод LogCommand через capsys (перехватчик stdout)
    captured = capsys.readouterr()
    assert "ERROR: MoveCommand: ошибка" in captured.out
    assert queue.empty() is True


def test_single_retry_then_log_scenario(capsys):
    queue = CommandQueue()
    registry = ExceptionHandlerRegistry()
    
    # первый сбой - повтор, второй сбой - в лог
    registry.register(BrokenMoveCommand, ValueError, RetryOnceHandler())
    registry.register(RetryOnceCommand, ValueError, RetryTwiceFailedHandler()) 
    
    queue.push(BrokenMoveCommand(obj="ship"))
    
    processor = CommandProcessor(queue, registry)
    processor.process()
    
    captured = capsys.readouterr()
    assert "ERROR: MoveCommand: ошибка" in captured.out


# 3. проверка работы конкретных обработчиков
def test_retry_once_handler_returns_retry_command():
    handler = RetryOnceHandler()
    mock_cmd = Mock(spec=Command)
    exc = ValueError("test")
    
    result = handler.handle(mock_cmd, exc)
    
    assert isinstance(result, RetryOnceCommand)
    assert result.cmd == mock_cmd


def test_retry_once_failed_handler_extracts_original_command():
    handler = RetryOnceFailedHandler()
    
    # неработающая команда
    original_cmd = Mock(spec=Command)
    failed_retry_cmd = RetryOnceCommand(original_cmd)
    exc = ValueError("test")
    
    result = handler.handle(failed_retry_cmd, exc)
    
    assert isinstance(result, RetryTwiceCommand)
    assert result.cmd == original_cmd


# нет обработчика в реестре
def test_no_handler_registered_leaves_queue_empty():
    queue = CommandQueue()
    registry = ExceptionHandlerRegistry() 
    
    queue.push(BrokenMoveCommand(obj="ship"))
    
    processor = CommandProcessor(queue, registry)
    processor.process() 
    
    assert queue.empty() is True
