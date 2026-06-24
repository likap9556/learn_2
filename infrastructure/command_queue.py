from collections import deque


class CommandQueue:

    def __init__(self):
        self._queue = deque()

    def push(self, cmd):
        self._queue.append(cmd)

    def pop(self):
        return self._queue.popleft()

    def empty(self):
        return len(self._queue) == 0