class QueueError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message


class ArgumentError(QueueError):
    def __init__(self):
        super().__init__("Invalid data format of max_size (must be int)")


class FullError(QueueError):
    def __init__(self):
        super().__init__("Queue is full")


class EmptyError(QueueError):
    def __init__(self):
        super().__init__("Queue is empty")
