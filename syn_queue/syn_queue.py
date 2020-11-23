import threading as thr

from syn_queue.errors.queue_error import QueueError
from syn_queue.errors.argument_error import ArgumentError


class Queue():
    def __init__(self, max_size=0):
        self.max_size = max_size
        self.__validate_max_size()
        self.infinite = max_size <= 0
        self.queue = []

    def __validate_max_size(self):
        if not isinstance(self.max_size, int):
            raise ArgumentError
