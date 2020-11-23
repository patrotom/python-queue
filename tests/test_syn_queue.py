import pytest

from syn_queue.syn_queue import Queue
from syn_queue.errors.argument_error import ArgumentError


class TestSynQueue():
    def test_init(self):
        with pytest.raises(ArgumentError):
            queue = Queue(max_size="err")
        
        queue = Queue()
        assert queue._Queue__max_size == 0
        assert queue._Queue__infinite == True

        queue = Queue(max_size=100)
        assert queue._Queue__max_size == 100
        assert queue._Queue__infinite == False
