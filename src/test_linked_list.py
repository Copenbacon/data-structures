"""This tests the linked_list module."""
import pytest

INSTANTIATION_TABLE = ["new_linked_list", "[0, 1, 2]", "red"],

PUSH_TABLE = ["new_linked_list", [0, 1, 2], 3, [3, 0, 1, 2]]


@pytest.mark.parametrize("list_name, nlist, result", INSTANTIATION_TABLE)
def test_linkedlist(list_name, nlist, result):
    """Test instantiationg LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList(nlist)
    assert list_name.color == 'red'


@pytest.mark.parametrize("list_name, nlist, value, result", PUSH_TABLE)
def test_push(list_name, nlist, value, result):
    """Test LinkedList push method."""
    from linked_list import LinkedList
    list_name = LinkedList(nlist)
    list_name.push(value)
    assert list_name.list == result
