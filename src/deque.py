"""Implement a double ended queue."""
from dll import DLL


class Deque(object):
    """Define the Deque class.

    It is important to note that the "tail" of our Deques is actually the front of the Deque.

    __init__(): initializes the Deque class as a composite of the DLL class.
    enqueue(): uses the push method from DLL to add nodes to the end of the Deque.
    dequeue(): removes a node from the front of the dequeue
    peek(): Looks at the front value of the Deque without removing it or advancing the view beyond it.
    size(): returns the size of the Deque.
    """

    def __init__(self, iterable=None):
        """Initiate the Deque as an instance of DLL."""
        self._container = DLL(iterable)

    def append(self, val):
        """Add value to the Deque at the end."""
        self._container.push(val)

    def appendleft(self, val):
        """Add value to the Deque at the beginning."""
        self._container.append(val)

    def popleft(self):
        """Remove the first value of the Deque."""
        return self._container.shift()

    def pop(self):
        """Remove a value from the end of the deque and returns it (raises an exception if the deque is empty)."""
        return self._container.pop()

    def peek(self):
        """Look at next value in the Deque without removing."""
        return self._container.head.val

    def peekleft(self):
        """Look at last value in the Deque without removing."""
        return self._container.tail.val

    def size(self):
        """How big the Deque is."""
        return self._container.size_of_list
