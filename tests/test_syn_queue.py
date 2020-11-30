import pytest

from syn_queue.syn_queue import SynQueue
from syn_queue.errors.queue_error import ArgumentError, EmptyError, FullError


@pytest.fixture
def sample_queue():
    queue = SynQueue(max_size=100)
    for i in range(100):
        queue.push(i)
    return queue


class TestSynQueue():
    def test_init(self):
        with pytest.raises(ArgumentError):
            SynQueue(max_size="err")
        
        queue = SynQueue()
        assert queue._SynQueue__max_size == 0
        assert queue._SynQueue__infinite == True

        queue = SynQueue(max_size=100)
        assert queue._SynQueue__max_size == 100
        assert queue._SynQueue__infinite == False

    def test_size(self, sample_queue):
        empty_queue = SynQueue()

        assert sample_queue.size() == 100
        assert empty_queue.size() == 0

    def test_empty(self, sample_queue):
        assert SynQueue().empty() == True
        assert sample_queue.empty() == False

    def test_full(self, sample_queue):
        assert SynQueue().full() == False
        assert sample_queue.full() == True

    def test_front(self, sample_queue):
        with pytest.raises(EmptyError):
            SynQueue().front()

        assert sample_queue.front() == 99

    def test_back(self, sample_queue):
        with pytest.raises(EmptyError):
            SynQueue().back()
        
        assert sample_queue.back() == 0

    def test_push(self):
        queue = SynQueue(max_size=5)

        for i in range(5):
            queue.push(i)
            assert queue.front() == i
            assert queue.back() == 0

        with pytest.raises(FullError):
            queue.push(5, block=False)

    def test_pop(self):
        queue = SynQueue(max_size=5)

        for i in range(5):
            queue.push(i)
        
        for i in range(4):
            assert queue.pop() == i
            assert queue.front() == 4
            assert queue.back() == i + 1
        
        assert queue.pop() == 4

        with pytest.raises(EmptyError):
            queue.pop(block=False)
