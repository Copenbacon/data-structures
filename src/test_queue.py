"""The test module for the Queue module."""
import pytest

ENQUEUE_TABLE = [
    [0]
]

ADDING_TABLE = [
    [0, [4, 3, 2, 1, 0]]
]


@pytest.fixture
def new_empty_queue():
    """Fixture to create a new empty queue list."""
    from queue import Queue
    new_queue = Queue()
    return new_queue


@pytest.fixture
def filled_queue():
    """Fixture to create a filled queue, to test against."""
    from queue import Queue
    new_filled_queue = Queue([4, 3, 2, 1])
    return new_filled_queue


def test_new_queue_exists(new_empty_queue):
    """Test whether instatiating Queue creates."""
    assert new_empty_queue.size() == 0 and new_empty_queue._container.head is None and new_empty_queue._container.tail is None


@pytest.mark.parametrize("val", ENQUEUE_TABLE)
def test_enqueue_increases_size_of_list(val, filled_queue):
    """Test that adding a node to end of queue increase size."""
    filled_queue.enqueue(val)
    assert filled_queue._container.head.val == val


@pytest.mark.parametrize("val, result", ADDING_TABLE)
def test_length_of_queue_when_using_enqueue(val, result, filled_queue):
    """Test adding a val via enqueue to see length of new queue list."""
    filled_queue.enqueue(val)
    assert filled_queue.size() == len(result) and filled_queue._container.head.val == val and filled_queue._container.tail.val == result[0]


def test_removing_the_first_val_in_queue_with_dequeue(filled_queue):
    """Test removing the first value in queue."""
    assert filled_queue.dequeue() == 4


def test_find_the_new_front_of_line_in_queue_with_dequeue(filled_queue):
    """Test removing the first value in queue."""
    filled_queue.dequeue()
    assert filled_queue._container.tail.val == 3
