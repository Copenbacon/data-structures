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
    ("This", "T")
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
