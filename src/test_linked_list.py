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
    (2, 2),
    (3, 3)
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
    list_name = LinkedList()
    list_name.push(val)
    assert list_name.head.val == result


@pytest.mark.parametrize("val1, val2", POP_TABLE)
def test_pop(val1, val2):
    """Test pop method to remove node off the front of a linked list."""
    from linked_list import LinkedList
    list_name = LinkedList()
    list_name.push(val1)
    list_name.push(val2)
    assert list_name.pop() == val1


@pytest.mark.parametrize("val1, result", SIZE_TABLE)
def test_size(val1, result):
    """Test size method in LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList()
    for number_to_push in range(val1):
        list_name.push(number_to_push)
    assert list_name.size() == result
