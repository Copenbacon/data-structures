"""Implement the Queue module."""
from dll import DLL


class Queue(object):
    """Define the Queue class."""

    def __init__(self, iterable=None):
        """Initiate the Queue as an instance of DLL."""
        self._container = DLL(iterable)

    def enqueue(self, val):
        """Add value to the Queue at the end."""
        self._container.append(val)

    def dequeue(self):
        """Remove the the head of the queue."""
        self._container.pop()

    def peek(self):
        """Look at next value in the Queue without removing."""
        return self._container.head.val

    def size(self):
        """How big the Queue is."""
        return self._container.size()
