"""This tests the linked_list module."""
import pytest


INSTANTIATION_TABLE = [
    ([3, 7, 5, 6, 4], 4),
    ((7, 6, 5, 4), 4),
    ([4], 4)
]

POP_TABLE = [
    ([7, 9], 9),
    ([33, 0, 10], 10),
    ((3, 2, 1, 34), 34),
]

SIZE_TABLE = [
    ([795]),
    ([2, 33]),
    ([3, 4, 5]),
    ((5, 3, 2, 23))
]

SEARCH_TABLE = [
    (3, [7, 3, 2], 3),
    (7, (7, 5, 5), 7),
    (3, {2, 1, 3}, 3),
    (8, [8, 8, 8], 8),
]

REMOVE_TABLE = [
    (3, [7, 3, 2], 7),
    (7, (8, 7, 5), 8),
    (5, {8, 7, 5}, 7),
]


def test_linkedlist():
    """Test instantiation LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList()
    assert list_name.size_of_list == 0


def test_non_iterable_raises_error():
    """Passing a non interable into new LinkedList raises TypeError."""
    from linked_list import LinkedList
    with pytest.raises(TypeError):
        list_name = LinkedList(4)


@pytest.mark.parametrize("val, result", INSTANTIATION_TABLE)
def test_head_is_last_value_in_table(val, result):
    """Test push method to add value to front of linked list."""
    from linked_list import LinkedList
    list_name = LinkedList(val)
    assert list_name.head.val == result


@pytest.mark.parametrize("val, result", POP_TABLE)
def test_pop(val, result):
    """Test pop method to remove node off the front of a linked list."""
    from linked_list import LinkedList
    list_name = LinkedList(val)
    assert list_name.pop() == result


@pytest.mark.parametrize("val", SIZE_TABLE)
def test_size(val):
    """Test size method in LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList(val)
    assert list_name.size() == len(val)


@pytest.mark.parametrize('val_to_search_for, val1, result', SEARCH_TABLE)
def test_search(val_to_search_for, val1, result):
    """Test search method to find value."""
    from linked_list import LinkedList
    search_list = LinkedList(val1)
    assert search_list.search(val_to_search_for).val == result


def test_search_raises_error_when_arg_not_found():
    """Make sure search returns a NameError when search term not found."""
    from linked_list import LinkedList
    search_list = LinkedList([8, 7, 6])
    with pytest.raises(ValueError):
        search_list.search(9)


@pytest.mark.parametrize("val_to_delete, val1, result", REMOVE_TABLE)
def test_remove(val_to_delete, val1, result):
    """Test remove method in LinkedList class."""
    from linked_list import LinkedList
    list_name = LinkedList(val1)
    list_name.remove(list_name.search(val_to_delete))
    assert list_name.size() == len(val1) - 1


def test_remove_last():
    """Test for removing the last value."""
    from linked_list import LinkedList
    list_name = LinkedList([5, 6, 7])
    list_name.remove(list_name.search(5))
    assert list_name.size() == 2


def test_remove_head():
    """Test for removing the last value."""
    from linked_list import LinkedList
    list_name = LinkedList([5, 6, 7])
    list_name.remove(list_name.search(7))
    assert list_name.size() == 2


def test_remove_not_in_list_raises_error():
    """Test that removing something not in list raises a NameError."""
    from linked_list import LinkedList
    list_name = LinkedList([5, 6, 7])
    with pytest.raises(ValueError):
        list_name.remove(list_name.search(9))


def test_display():
    """Test for displaying as a tuple."""
    from linked_list import LinkedList
    list_name = LinkedList([5, 6, '*adf'])
    assert list_name.display() == '(*adf, 6, 5)'
