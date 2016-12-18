"""This is the module to push and pop off a stack."""
from linked_list import LinkedList


class Stack(object):
    """Define stack class.

    __init__(): Initiate the Stack as a instance of LinkedList.
    pop(): Remove the top element from stack and returns it.
    push(): Add a value to the top of the stack.
    _size(): Return the length of the stack.
    _is_empty(): Return true if the stack is empty.
    """

    def __init__(self, iterable=None):
        """.Initiate the Stack as a instance of LinkedList."""
        self._container = LinkedList(iterable)

    def pop(self):
        """Remove the top element from stack and returns it."""
        return self._container.pop()

    def push(self, val):
        """Add a value to the top of the stack."""
        self._container.push(val)

    def _size(self):
        """Return the length of the stack."""
        return self._container.size()

    def __len__(self):
        """A length method to call on the Stack."""
        return self._size()

    def _is_empty(self):
        """Return true if the stack is empty."""
        if self._container.size() == 0:
            return True
