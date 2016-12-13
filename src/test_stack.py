"""This is the test for stack module."""
import pytest


PUSH_TABLE = [
    [[1, 2, 3], 4, 4],
    ["Foo to the bar", 5, 15],
    [("a", "b", "c"), (5,), 4],
    [{"one": 1, "two": 2}, {"three": 3}, 3],
]

POP_TABLE = [
    [[1, 2, 3], 2],
    ["Foo to the bar", 13],
    [("a", "b", "c"), 2],
    [{"one": 1, "two": 2}, 1],
]


@pytest.fixture
def new_stack():
    """Instantiate a new stack with no args."""
    from stack import Stack
    this_stack = Stack()
    return this_stack


@pytest.mark.parametrize("iterable, val, result", PUSH_TABLE)
def test_push(iterable, val, result):
    """Test the push method increases the size of the stack."""
    from stack import Stack
    stack_push = Stack(iterable)
    stack_push.push(val)
    assert stack_push._size() == result


@pytest.mark.parametrize("iterable, result", POP_TABLE)
def test_pop(iterable, result):
    """Test the pop method decreases the size of the stack."""
    from stack import Stack
    stack_pop = Stack(iterable)
    stack_pop.pop()
    assert stack_pop._size() == result


def test_new_empty_stack_is_empty(new_stack):
    """Test a new stack is empty."""
    assert new_stack._is_empty() is True
