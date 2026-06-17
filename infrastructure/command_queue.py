from collections import deque


class CommandQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, cmd):
        self.queue.append(cmd)

    def pop(self):
        return self.queue.popleft()

    def empty(self):
        return len(self.queue) == 0