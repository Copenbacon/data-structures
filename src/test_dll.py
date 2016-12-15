"""This is the test module for the dll module."""
import pytest
# encoding: utf-8


TAIL_TABLE = [
    ([3, 4, 5, 6], 3),
    ([9], 9),
    ((7, 8), 7),
    ("This", "T")
]

PUSH_TABLE = [
    ([13, 14, 15, 16], 17),
    ([9], 8),
    ((7, 8), 12),
    ("This", "T"),
]

POP_TABLE = [
    ([13, 14, 15, 16], 16),
    ([9], 9),
    ((7, 8), 8),
    ("This", "s"),
]

APPEND_TABLE = [
    ([13, 14, 15, 16], 17),
    ([9], 8),
    ((7, 8), 12),
    ("This", "T"),
]

SHIFT_TABLE = [
    ([13, 14, 15, 16], 13),
    ((7, 8), 7),
    ("This", "T"),
    ([9], 9),
]

REMOVE_TABLE = [
    ((2, 4, 6, 8), 4),
    ((17, 21, 25, 29), 21),
    ([33, 43, 53, 63], 53),
    ([33, 43, 53, 63], 63),
    ([33, 43, 53, 63], 33),
    (["This", "is", "my", "life"], "This"),
]

SEARCH_TABLE = [
    ((2, 4, 6, 8), 4),
    ((17, 21, 25, 29), 21),
    ([33, 43, 53, 63], 43),
    (["This", "is", "my", "life"], "This"),
]

@pytest.fixture
def new_empty_dll():
    """Fixture to create new doubly-linked list."""
    from dll import DLL
    new_dll = DLL()
    return new_dll


def test_new_dll_exists(new_empty_dll):
    """Test the creation of a new doubly-linked list."""
    assert new_empty_dll.head is None


def test_tail_when_empty(new_empty_dll):
    """Test an empty dll to make sure tail doesn't exist."""
    assert new_empty_dll.tail is None


def test_init_type_error():
    """Test for error when 1 value, non-iterable, is initialized in list."""
    from dll import DLL
    with pytest.raises(TypeError):
        new_dll = DLL(1)


@pytest.mark.parametrize("val, result", TAIL_TABLE)
def test_tail_with_values_in_dll(val, result):
    """Test to see if tail exists with a dll that has nodes."""
    from dll import DLL
    new_dll = DLL(val)
    assert new_dll.tail.val == result


@pytest.mark.parametrize("iterable, val", PUSH_TABLE)
def test_push(iterable, val):
    """Test inserting a value to head of a list."""
    from dll import DLL
    new_dll = DLL(iterable)
    new_dll.push(val)
    assert new_dll.head.val == val


@pytest.mark.parametrize("iterable, val", APPEND_TABLE)
def test_append(iterable, val):
    """Test inserting a value to head of a list."""
    from dll import DLL
    new_dll = DLL(iterable)
    new_dll.append(val)
    assert new_dll.tail.val == val


def test_append_when_dll_empty(new_empty_dll):
    """Test appending a new value to an empty list sets the head and tail for the list."""
    new_empty_dll.append(9)
    assert new_empty_dll.head.val == 9 and new_empty_dll.tail.val == 9


@pytest.mark.parametrize("iterable, result", POP_TABLE)
def test_pop_when_list_has_data(iterable, result):
    """Test that popping a list with data returns the value popped."""
    from dll import DLL
    new_dll = DLL(iterable)
    assert new_dll.pop() == result


def test_pop_when_empty(new_empty_dll):
    """Test that popping an empty list returns an index error."""
    with pytest.raises(IndexError):
        new_empty_dll.pop()


@pytest.mark.parametrize("iterable, result", SHIFT_TABLE)
def test_shift(iterable, result):
    """Test shifting a value from tail of a list."""
    from dll import DLL
    new_dll = DLL(iterable)
    assert new_dll.shift() == result


def test_shift_when_empty(new_empty_dll):
    """Test that shifting an empty list returns an index error."""
    with pytest.raises(IndexError):
        new_empty_dll.shift()


@pytest.mark.parametrize("iterable, val", REMOVE_TABLE)
def test_remove_val_in_list(iterable, val):
    """Test searching and removing a val in a list."""
    from dll import DLL
    new_dll = DLL(iterable)
    new_dll.remove(val)
    assert new_dll.size_of_list == len(iterable) - 1


def test_remove_when_not_in_list():
    """Test removing a val that is not in the list."""
    from dll import DLL
    new_dll = DLL((7, 8, 9, 10, 12))
    with pytest.raises(NameError):
        new_dll.remove(11)


def test_remove_from_empty_list(new_empty_dll):
    """Test remove from empty list."""
    with pytest.raises(NameError):
        new_empty_dll.remove(11)


def test_search_empty_list(new_empty_dll):
    """Test Searching an empty list."""
    with pytest.raises(NameError):
        new_empty_dll.search(11)


@pytest.mark.parametrize("iterable, val", SEARCH_TABLE)
def test_search_val_in_list(iterable, val):
    """Test searching and removing a val in a list."""
    from dll import DLL
    new_dll = DLL(iterable)
    assert new_dll.search(val).val == val
