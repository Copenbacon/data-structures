"""Implement the Queue module."""
from dll import DLL


class Queue(object):
    """Define the Queue class."""

    def __init__(self, iterable=None):
        """Initiate the Queue as an instance of DLL."""
        self._container = DLL(iterable)

    def enqueue(self, val):
        """Add value to the Queue at the end."""
        self._container.push(val)

    def dequeue(self):
        """Remove the first value of the queue."""
        return self._container.shift()

    def peek(self):
        """Look at next value in the Queue without removing."""
        return self._container.tail.val

    def size(self):
        """How big the Queue is."""
        return self._container.size_of_list
