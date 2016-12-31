"""The test module for the Deque module."""
import pytest

APPEND_TABLE = [
    [0],
]

ADDING_TABLE = [
    [0, [4, 3, 2, 1, 0]],
]

APPEND_LEFT_TABLE = [
    [0],
]

ADDING_LEFT_TABLE = [
    [0, [4, 3, 2, 1, 0]],
]

POP_TABLE = [
    ((0, 1, 2, 3, 4)),
    ([9, 45, "lol", "b"]),
]

PEEK_TABLE = (
    ((0, 1, 2, 3, 4)),
    ([9, 45, "lol", "b"]),
    [4, 3, 2, 1, 0],
    ("This string is iterable"),
)

POP_LEFT_TABLE = [
    ((0, 1, 2, 3, 4)),
    ([9, 45, "lol", "b"]),
]

PEEK_LEFT_TABLE = (
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
def new_empty_deque():
    """Fixture to create a new empty deque list."""
    from deque import Deque
    new_deque = Deque()
    return new_deque


@pytest.fixture
def filled_deque():
    """Fixture to create a filled queue, to test against."""
    from deque import Deque
    new_filled_deque = Deque([4, 3, 2, 1])
    return new_filled_deque


def test_new_deque_exists(new_empty_deque):
    """Test whether instatiating Queue creates."""
    assert new_empty_deque.size() == 0 and new_empty_deque._container.head is None and new_empty_deque._container.tail is None


@pytest.mark.parametrize("val", APPEND_TABLE)
def test_append_increases_size_of_list(val, filled_deque):
    """Test that adding a node to end of deque increase size."""
    filled_deque.append(val)
    assert filled_deque._container.head.val == val


@pytest.mark.parametrize("val, result", ADDING_TABLE)
def test_length_of_deque_when_using_append(val, result, filled_deque):
    """Test adding a val via append updates head/tail."""
    filled_deque.append(val)
    assert filled_deque.size() == len(result) and filled_deque._container.head.val == val and filled_deque._container.head.val == result[-1]


@pytest.mark.parametrize("val", APPEND_LEFT_TABLE)
def test_append_left_increases_size_of_list(val, filled_deque):
    """Test that adding a node to front of deque increases size."""
    filled_deque.appendleft(val)
    assert filled_deque._container.tail.val == val


@pytest.mark.parametrize("val, result", ADDING_LEFT_TABLE)
def test_length_of_deque_when_using_append_left(val, result, filled_deque):
    """Test adding a val via append left updates head/tail."""
    filled_deque.appendleft(val)
    assert filled_deque.size() == len(result) and filled_deque._container.tail.val == result[-1] and filled_deque._container.tail.val == val


def test_removing_the_last_val_in_deque(filled_deque):
    """Test removing the last value in queue and returning."""
    assert filled_deque.pop() == 1


def test_find_the_new_front_of_line_in_deque_with_pop(filled_deque):
    """Test removing the last value in deque."""
    filled_deque.pop()
    assert filled_deque._container.tail.val == 4


def test_removing_the_first_val_in_deque(filled_deque):
    """Test removing the first value in queue and returning."""
    assert filled_deque.popleft() == 4


def test_find_the_new_back_of_line_in_deque_with_popleft(filled_deque):
    """Test removing the first value in deque."""
    filled_deque.popleft()
    assert filled_deque._container.head.val == 1


@pytest.mark.parametrize("iterable", POP_TABLE)
def test_deque_works_on_diff_iterables(iterable):
    """Testing dequeue method on a variety of iterables."""
    from deque import Deque
    new_deque = Deque(iterable)
    assert new_deque.pop() == iterable[-1] and new_deque._container.tail.val == iterable[0] and new_deque._container.head.val == iterable[-2]


def test_that_peek_returns_tail(filled_deque):
    """Testing that peek() method returns the proper value."""
    assert filled_deque.peek() == 1


def test_that_peekleft_returns_head(filled_deque):
    """Testing that peek() method returns the proper value."""
    assert filled_deque.peekleft() == 4


@pytest.mark.parametrize("iterable", PEEK_TABLE)
def test_that_peek_returns_head_from_list_of_iterables(iterable):
    """Testing that peek() method returns the proper value."""
    from deque import Deque
    new_deque = Deque(iterable)
    assert new_deque.peek() == new_deque.pop()


@pytest.mark.parametrize("iterable", PEEK_TABLE)
def test_that_peekleft_returns_tail_from_list_of_iterables(iterable):
    """Testing that peek() method returns the proper value."""
    from deque import Deque
    new_deque = Deque(iterable)
    assert new_deque.peekleft() == new_deque.popleft()


@pytest.mark.parametrize("iterable, result", SIZE_TABLE)
def test_for_size_when_filled(iterable, result):
    """Checking for table size when passed in iterables."""
    from deque import Deque
    new_deque = Deque(iterable)
    assert new_deque.size() == result


def test_for_size_0_when_empty(new_empty_deque):
    """Checking size is 0."""
    assert new_empty_deque.size() == 0


def test_that_pop_empty_table_raises_error(new_empty_deque):
    """Make sure popping from an empty table raises an error."""
    with pytest.raises(IndexError):
        new_empty_deque.pop()


def test_that_popleft_empty_table_raises_error(new_empty_deque):
    """Make sure poplefting from an empty table raises an error."""
    with pytest.raises(IndexError):
        new_empty_deque.popleft()


def test_init_type_error():
    """Test for error when 1 value, non-iterable, is initialized in Queue."""
    from deque import Deque
    with pytest.raises(TypeError):
        new_deque = Deque(1)


def test_peek_return_none_when_empty(new_empty_deque):
    """Peeking should return None when empty."""
    assert new_empty_deque.peek() is None


def test_peekleft_return_none_when_empty(new_empty_deque):
    """Peeking left should return None when empty."""
    assert new_empty_deque.peekleft() is None

