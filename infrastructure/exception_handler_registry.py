class ExceptionHandlerRegistry:

    def __init__(self):
        self._handlers = {}

    def register(self, cmd_type, exc_type, handler):
        self._handlers[(cmd_type, exc_type)] = handler

    def get_handler(self, cmd, exc):

        for (cmd_type, exc_type), handler in self._handlers.items():

            if isinstance(cmd, cmd_type) and isinstance(exc, exc_type):
                return handler

        return None