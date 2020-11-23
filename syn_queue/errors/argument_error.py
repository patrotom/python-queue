from syn_queue.errors.queue_error import QueueError


class ArgumentError(QueueError):
    def __init__(self):
        super().__init__("Invalid data format of max_size (must be int)")
