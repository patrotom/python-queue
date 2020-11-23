import pytest

from syn_queue.syn_queue import SynQueue
from syn_queue.errors.argument_error import ArgumentError


class TestSynQueue():
    def test_init(self):
        with pytest.raises(ArgumentError):
            queue = SynQueue(max_size="err")
        
        queue = SynQueue()
        assert queue._SynQueue__max_size == 0
        assert queue._SynQueue__infinite == True

        queue = SynQueue(max_size=100)
        assert queue._SynQueue__max_size == 100
        assert queue._SynQueue__infinite == False
