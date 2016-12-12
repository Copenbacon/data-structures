"""This tests the linked_list module."""
import pytest

SOME_TABLE = []


@pytest.mark.parametrize("list, result", SOME_TABLE)
def test_linkedlist(list, result):
    """Test instantiationg LinkedList class."""
    from linked_list import LinkedList
    assert LinkedList(list) == result
