"""This is the test module for the dll module."""
import pytest
# encoding: utf-8


@pytest.fixture
def new_empty_dll():
    """Fixture to create new doubly-linked list."""
    from dll import DLL
    new_dll = DLL()
    return new_dll


def test_new_dll_exists(new_empty_dll):
    """Test the creation of a new doubly-linked list."""
    assert new_empty_dll.head is None and new_empty_dll.size_of_list == 0 and new_empty_dll.head.val is None and new_empty_dll.head.next is None


# @pytest.mark.parametrize("val, result", PUSH_TABLE)
# def test_push(val, result, new_empty_dll):
#     """Test inserting a value to head of a list."""
#     assert push()
