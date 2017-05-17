"""Test the Binary Heap Module."""
import pytest


BIN_HEAP_TABLE = [
    [[9, 8, 7, 6, 5], [5, 6, 8, 9, 7]],
    [[1, 3, 7, 5, 9, 0], [0, 3, 1, 5, 9, 7]],
    [[50, 1000, 0, 5, 2, 99, 42, 1, 60], [0, 1, 42, 2, 5, 99, 50, 1000, 60]],
    [[20, 19, 15, 10, 17, 25, 4, 8], [4, 8, 10, 15, 17, 25, 19, 20]]
]

BIN_HEAP_POP_TABLE = [
    [[9, 8, 7, 6, 5], 5],
    [[1, 3, 7, 5, 9, 0], 0],
    [[50, 1000, 0, 5, 2, 99, 42, 1, 60], 0],
    [[20, 19, 15, 10, 17, 25, 4, 8], 4]
]

ITER_TABLE = (
    ((2, 6, 7, 9)),
    ([23, 45, 72]),
    ({"val1": 23, "val3": 45, "val2": 76})
)


@pytest.fixture
def empty_bin_heap():
    """Fixture for empty Binary Heap."""
    from binheap import BBinnyHeap
    empty_heap = BBinnyHeap()
    return empty_heap


def test_empty_binheap_is_empty(empty_bin_heap):
    """Make sure the empty binheap is empty."""
    assert empty_bin_heap.list_heap == []


@pytest.mark.parametrize("iterable, result", BIN_HEAP_TABLE)
def test_bin_heap_takes_iterable(iterable, result):
    """Binheap should take an interable."""
    from binheap import BBinnyHeap
    new_heap = BBinnyHeap(iterable)
    assert new_heap.list_heap == result


def test_push_increases_size(empty_bin_heap):
    """Test pushing increases Heap Size."""
    empty_bin_heap.push(3)
    assert empty_bin_heap.size == 1


def test_push_adds_value(empty_bin_heap):
    """Test that value pushed is in heap list."""
    empty_bin_heap.push(3)
    assert empty_bin_heap.list_heap == [3]


@pytest.mark.parametrize("iterable", ITER_TABLE)
def test_pushing_an_iterable_raises_error(iterable, empty_bin_heap):
    """Make sure they can't push iterables except on initialization."""
    with pytest.raises(TypeError):
        empty_bin_heap.push(iterable)


@pytest.mark.parametrize("iterable, result", BIN_HEAP_TABLE)
def test_bin_heap_takes_multiple_pushes(iterable, result, empty_bin_heap):
    """Binheap should take an interable."""
    for val in iterable:
        empty_bin_heap.push(val)
    assert empty_bin_heap.list_heap == result


@pytest.mark.parametrize("iterable, result", BIN_HEAP_POP_TABLE)
def test_bin_heap_removes_values(iterable, result):
    """Popping from binheap should remove first value."""
    from binheap import BBinnyHeap
    new_heap = BBinnyHeap(iterable)
    assert new_heap.pop() == result


def test_popping_empty_heap_produces_error(empty_bin_heap):
    """Popping an empty heap should produce an index error."""
    with pytest.raises(IndexError):
        empty_bin_heap.pop()
