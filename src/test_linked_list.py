"""This tests the linked_list module."""
import pytest

INSTANTIATION_TABLE = [
    ("new_linked_list"),
]


PUSH_TABLE = [
    (3, 3),
    (4, 4)
]


POP_TABLE = [
    (7, 9),
    (33, 10)
]


SIZE_TABLE = [
    (795, 1),
    ([2, 33], 2),
    ([3, 4, 5], 3),
]


SEARCH_TABLE = [
    (3, 7, 3, 2, 3),
    (7, 7, 5, 5, 7),
    (3, 2, 1, 3, 3),
    (9, 8, 8, 9, 9),
    (8, 8, 8, 8, 8),
]

REMOVE_TABLE = [
    (3, 7, 3, 2, 7),
    (7, 8, 7, 5, 8),
    (5, 8, 7, 5, 7),
]


@pytest.mark.parametrize("list_name", INSTANTIATION_TABLE)
def test_linkedlist(list_name):
    """Test instantiation LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList()
    assert list_name.size_of_list == 0


@pytest.mark.parametrize("val, result", PUSH_TABLE)
def test_push(val, result):
    """Test push method to add value to front of linked list."""
    from linked_list import LinkedList
    list_name = LinkedList(val)
    assert list_name.head.val == result


@pytest.mark.parametrize("val1, val2", POP_TABLE)
def test_pop(val1, val2):
    """Test pop method to remove node off the front of a linked list."""
    from linked_list import LinkedList
    list_name = LinkedList(val1)
    list_name.push(val2)
    assert list_name.pop() == val2


@pytest.mark.parametrize("val1, result", SIZE_TABLE)
def test_size(val1, result):
    """Test size method in LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList(val1)
    assert list_name.size() == result


@pytest.mark.parametrize('val_to_search_for, val1, val2, val3, result', SEARCH_TABLE)
def test_search(val_to_search_for, val1, val2, val3, result):
    """Test search method to find value."""
    from linked_list import LinkedList
    search_list = LinkedList(val1)
    search_list.push(val2)
    search_list.push(val3)
    assert search_list.search(val_to_search_for).val == result


@pytest.mark.parametrize("val_to_delete, val1, val2, val3, result", REMOVE_TABLE)
def test_remove(val_to_delete, val1, val2, val3, result):
    """Test remove method in LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList(val1)
    list_name.push(val2)
    list_name.push(val3)
    assert_result = list_name.remove(val_to_delete)
    assert assert_result.val == result


def test_remove_last():
    """Test for removing the last value."""
    from linked_list import LinkedList
    list_name = LinkedList(5)
    list_name.push(6)
    list_name.push(7)
    assert list_name.remove(5) is None


def test_display():
    """Test for displaying as a tuple."""
    from linked_list import LinkedList
    list_name = LinkedList(5)
    list_name.push(6)
    list_name.push('*adf')
    assert list_name.display() == '(*adf,6,5,)'
