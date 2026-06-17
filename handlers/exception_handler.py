from abc import ABC, abstractmethod

class ExceptionHandler(ABC):

    @abstractmethod
    def handle(self, cmd, exc, queue):
        pass