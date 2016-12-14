"""This is the test for stack module."""
import pytest
import random

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

PUSH_IT_TABLE = [
    [[1, 2, 3], 4],
    ["Foo to the bar", 5],
    [("a", "b", "c"), (5,)],
    [{"one": 1, "two": 2}, {"three": 3}],
]

PUSH_STACK_TABLE = [
    [[1, 2, 3], 4],
    ["Foo to the bar", 5],
    [("a", "b", "c"), (5,)],
    [{"one": 1, "two": 2}, {"three": 3}],
]

SIZE_DECREASES_TABLE = [
    [7, 5],
    [1000, 500],
    [random.randint(75, 150), random.randint(0, 75)],
    [1, 1]
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


@pytest.mark.parametrize("iterable, val", PUSH_IT_TABLE)
def test_push_it(iterable, val):
    """Test the push method adds a value to top of stack."""
    from stack import Stack
    stack_push = Stack(iterable)
    stack_push.push(val)
    assert stack_push._container.head.val == val


@pytest.mark.parametrize("iterable, val", PUSH_STACK_TABLE)
def test_push_stack(iterable, val):
    """Test the push method to see entire stack is updated with new value."""
    from stack import Stack
    stack_push = Stack(iterable)
    stack_push.push(val)
    assert str(val) in stack_push._container.display()


@pytest.mark.parametrize("times_pushed, times_popped", SIZE_DECREASES_TABLE)
def test_size_decreases(times_pushed, times_popped):
    """When I pop, I reduce the list size."""
    from stack import Stack
    size_stack = Stack()
    for i in range(times_pushed):
        size_stack.push(random.randint(0, 10))
    for i in range(times_popped):
        size_stack.pop()
    assert size_stack._size() == times_pushed - times_popped
