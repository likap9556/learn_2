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

                if not handler:
                    continue

                new_cmd = handler.handle(cmd, exc)

                if new_cmd:
                    self.queue.push(new_cmd)