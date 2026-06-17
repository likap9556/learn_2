class CommandProcessor:
    def __init__(self, queue, registry):
        self.queue = queue
        self.registry = registry

    def process(self):
        while not self.queue.empty():
            cmd = self.queue.pop()

            try:
                cmd.execute()

            except Exception as exc:
                handler = self.registry.get_handler(cmd, exc)

                if handler:
                    handler.handle(cmd, exc, self.queue)