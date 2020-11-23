import threading
from collections import deque

from syn_queue.errors.queue_error import QueueError
from syn_queue.errors.argument_error import ArgumentError


class SynQueue():
    def __init__(self, max_size=0):
        self.__init_attrs(max_size)
        self.__init_threading()

    def size(self):
        with self.__lock:
            return self.__size()

    def empty(self):
        with self.__lock:
            return self.__size() == 0

    def full(self):
        with self.__lock:
            return self.__size() == self.__max_size()

    def __init_attrs(self, max_size):
        self.__max_size = max_size
        self.__validate_max_size()
        self.__infinite = max_size <= 0
        self.__queue = deque(max_size)

    def __init_threading(self):
        self.__lock = threading.Lock()

    def __validate_max_size(self):
        if not isinstance(self.__max_size, int):
            raise ArgumentError

    def __size(self):
        return len(self.__queue)
