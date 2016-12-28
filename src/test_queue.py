"""The test module for the Queue module."""
import pytest

ENQUEUE_TABLE = [
    [0],
]

ADDING_TABLE = [
    [0, [4, 3, 2, 1, 0]],
]

DEQUEUE_TABLE = [
    ((0, 1, 2, 3, 4)),
    ([9, 45, "lol", "b"]),
]

PEEK_TABLE = (
    ((0, 1, 2, 3, 4)),
    ([9, 45, "lol", "b"]),
    [4, 3, 2, 1, 0],
    ("This string is iterable"),
)

SIZE_TABLE = [
    [[4, 3, 2, 1, 0], 5],
    ((4, 3, 2, 1, 0, -1), 6),
    ("this is a string of chars", 25)
]


@pytest.fixture
def new_empty_queue():
    """Fixture to create a new empty queue list."""
    from queue_ import Queue
    new_queue = Queue()
    return new_queue


@pytest.fixture
def filled_queue():
    """Fixture to create a filled queue, to test against."""
    from queue_ import Queue
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


@pytest.mark.parametrize("iterable", DEQUEUE_TABLE)
def test_dequeue_works_on_diff_iterables(iterable):
    """Testing dequeue method on a variety of iterables."""
    from queue_ import Queue
    new_queue = Queue(iterable)
    assert new_queue.dequeue() == iterable[0] and new_queue._container.tail.val == iterable[1] and new_queue._container.head.val == iterable[-1]


def test_that_peek_returns_tail(filled_queue):
    """Testing that peek() method returns the proper value."""
    assert filled_queue.peek() == 4


@pytest.mark.parametrize("iterable", PEEK_TABLE)
def test_that_peek_returns_tail_from_list_of_iterables(iterable):
    """Testing that peek() method returns the proper value."""
    from queue_ import Queue
    new_queue = Queue(iterable)
    assert new_queue.peek() == iterable[0]


@pytest.mark.parametrize("iterable, result", SIZE_TABLE)
def test_for_size_when_filled(iterable, result):
    """Checking for table size when passed in iterables."""
    from queue_ import Queue
    new_queue = Queue(iterable)
    assert new_queue.size() == result


def test_for_size_0_when_empty(new_empty_queue):
    """Checking size is 0."""
    assert new_empty_queue.size() == 0


def test_that_dequeueing_empty_table_raises_error(new_empty_queue):
    """Make sure dequeueing from an empty table raises an error."""
    with pytest.raises(AttributeError):
        new_empty_queue.dequeue()


def test_init_type_error():
    """Test for error when 1 value, non-iterable, is initialized in Queue."""
    from queue_ import Queue
    with pytest.raises(TypeError):
        new_queue = Queue(1)


def test_that_peeking_empty_queue_raises_error(new_empty_queue):
    """Make sure peeking an empty Queue raises error."""
    with pytest.raises(AttributeError):
        new_empty_queue.peek()
