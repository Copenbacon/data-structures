"""Implement the Queue module."""
from dll import DLL


class Queue(object):
    """Define the Queue class.

    It is important to note that the "tail" of our queue is actually the front of the Queue.

    __init__(): initializes the Queue class as a composite of the DLL class.
    enqueue(): uses the push method from DLL to add nodes to the end of the Queue.
    dequeue(): removes a node from the front of the dequeue
    peek(): Looks at the front value of the Queue without removing it or advancing the view beyond it.
    size(): returns the size of the Queue.
    """

    def __init__(self, iterable=None):
        """Initiate the Queue as an instance of DLL."""
        self._container = DLL(iterable)

    def enqueue(self, val):
        """Add value to the Queue at the end."""
        self._container.push(val)

    def dequeue(self):
        """Remove the first value of the queue."""
        try:
            return self._container.shift()
        except AttributeError:
            raise AttributeError("Cannot dequeue from an empty Queue.")

    def peek(self):
        """Look at next value in the Queue without removing."""
        try:
            return self._container.tail.val
        except AttributeError:
            raise AttributeError("Queue is empty.")

    def size(self):
        """How big the Queue is."""
        return self._container.size_of_list
