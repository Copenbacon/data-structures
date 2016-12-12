"""This tests the linked_list module."""
import pytest

INSTANTIATION_TABLE = [
    ("new_linked_list"),
]


@pytest.mark.parametrize("list_name", INSTANTIATION_TABLE)
def test_linkedlist(list_name):
    """Test instantiationg LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList()
    assert list_name.size == 0
