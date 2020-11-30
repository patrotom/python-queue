import threading
from collections import deque

from syn_queue.errors.queue_error import ArgumentError, FullError, EmptyError


class SynQueue():
    def __init__(self, max_size=0):
        self.__init_attrs(max_size)
        self.__init_threading()

    def size(self):
        with self.__lock:
            return self.__size()

    def empty(self):
        with self.__lock:
            return self.__empty()

    def full(self):
        with self.__lock:
            return self.__full()

    def front(self):
        with self.__lock:
            try:
                return self.__queue[0]
            except IndexError:
                raise EmptyError

    def back(self):
        with self.__lock:
            try:
                return self.__queue[-1]
            except IndexError:
                raise EmptyError

    def push(self, item, block=True, timeout=None):
        with self.__full_cond:
            if self.__full():
                if block:
                    if not self.__full_cond.wait_for(
                        lambda: not self.__full(),
                        timeout=timeout
                    ):
                        raise FullError
                else:
                    raise FullError
            
            self.__queue.appendleft(item)
            self.__empty_cond.notify()
    
    def pop(self, block=True, timeout=None):
        with self.__empty_cond:
            if self.__empty():
                if block:
                    if not self.__empty_cond.wait_for(
                        lambda: not self.__empty(),
                        timeout=timeout
                    ):
                        raise EmptyError
                else:
                    raise EmptyError
            
            item = self.__queue.pop()
            self.__full_cond.notify()

            return item

    def __init_attrs(self, max_size):
        self.__max_size = max_size
        self.__validate_max_size()
        self.__infinite = max_size <= 0
        self.__queue = deque() if self.__infinite else deque(maxlen=max_size)

    def __init_threading(self):
        self.__lock = threading.Lock()
        self.__full_cond = threading.Condition(self.__lock)
        self.__empty_cond = threading.Condition(self.__lock)

    def __validate_max_size(self):
        if not isinstance(self.__max_size, int):
            raise ArgumentError

    def __size(self):
        return len(self.__queue)
    
    def __empty(self):
        return self.__size() == 0

    def __full(self):
        return (self.__size() >= self.__max_size) and (not self.__infinite)
