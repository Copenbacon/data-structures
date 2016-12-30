"""Test the priorityQ module, pq.py."""
import pytest
import sys

if sys.version_info[0] == 3:
    from math import inf
else:
    inf = float("inf")

INIT_TABLE = [
    [[(1, 0), (3, 4), [5, 6], [7, 8]], {0: [1], 4: [3], 6: [5], 8: [7]}],
    [[1], {-inf: [1]}],
    [1, {-inf: [1]}],
    [[{1: 1}], {-inf: [[{1: 1}]]}],
    [[({1: 1}, 1)], {1: [{1: 1}]}],
]

POP_TABLE = [
    [[(1, 0), (3, 4), [5, 6], [7, 8], (3, 0)], 4],
    [[1], 0],
    [1, 0],
]

POP_TABLE2 = [
    [[(1, 0), (3, 4), [5, 6], [7, 8], (3, 0)], 1],
    [[1], 1],
    [1, 1],
]

PEEK_TABLE = [
    [[(1, 0), (3, 4), [5, 6], [7, 8], (3, 0)], '0: 1'],
    [[1, 2, 3, 4, 5], '-inf: 1'],
]


@pytest.fixture
def new_empty_priority_q():
    """Empty PikaQ fixture."""
    from pq import PikaQ
    return PikaQ()


def test_empty_initialization(new_empty_priority_q):
    """Test that the empty priority queue exists."""
    assert len(new_empty_priority_q.pq) == 0


@pytest.mark.parametrize("vals, result", INIT_TABLE)
def test_initialization_with_values(vals, result):
    """Test that a PQ can be initialized with values."""
    from pq import PikaQ
    new_pq = PikaQ(vals)
    assert new_pq.pq == result

if sys.version_info[0] == 3:
    def test_value_error():
        """Raise a value error when initializing with just a string."""
        from pq import PikaQ
        with pytest.raises(ValueError):
            new_pq = PikaQ("Some string right here.")


def test_insert_actually_inserts(new_empty_priority_q):
    """Inserting a single value should create a -inf node, which is the base and highest priority."""
    new_empty_priority_q.insert(1)
    assert new_empty_priority_q.pq == {-inf: [1]}


def test_insert_2_vals_actually_inserts(new_empty_priority_q):
    """Inserting two args should create a node with the second arg as a new priority."""
    new_empty_priority_q.insert(1, 2)
    assert new_empty_priority_q.pq == {2: [1]}


def test_insert_bool_raise_error(new_empty_priority_q):
    """Inserting a boolean as a priority should raise a TypeError."""
    with pytest.raises(TypeError):
        new_empty_priority_q.insert(2, True)


@pytest.mark.parametrize("vals, result", POP_TABLE)
def test_popping_removes_the_highest_priority_item(vals, result):
    """Test that a PQ can be initialized with values."""
    from pq import PikaQ
    new_pq = PikaQ(vals)
    new_pq.pop()
    assert len(new_pq.pq) == result


@pytest.mark.parametrize("vals, result", POP_TABLE2)
def test_popping_returns_value_popped(vals, result):
    """Popping a pq should return the value popped."""
    from pq import PikaQ
    new_pq = PikaQ(vals)
    assert new_pq.pop() == result


def test_popping_empty_raises_error(new_empty_priority_q):
    """Test that an error is raised and handled when popping an empty Priority Q."""
    with pytest.raises(IndexError):
        new_empty_priority_q.pop()


@pytest.mark.parametrize("vals, result", PEEK_TABLE)
def test_peeking_reveals_the_highest_priority_item(vals, result):
    """Test that peek() reveals the next highest priority item."""
    from pq import PikaQ
    new_pq = PikaQ(vals)
    assert new_pq.peek() == result


def test_peeking_empty_reveals_error(new_empty_priority_q):
    """Test that peek() on empty Priority Q reveals an error."""
    assert new_empty_priority_q.peek() == "Nothing, Priority Q is empty!"