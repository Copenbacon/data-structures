"""Implement a double ended queue."""
from dll import DLL


class Deque(object):
    """Define the Deque class.

    It is important to note that the "tail" of our Deques is actually the front of the Deque.

    __init__(): initializes the Deque class as a composite of the DLL class.
    append(): uses the push method from DLL to add nodes to the end of the Deque.
    appendleft(): uses the append method from DLL to add nodes to the start of the Deque.
    popleft(): removes a node from the front of the dequeue
    pop(): removes a node from the end of the dequeue
    peek(): Looks at the front value of the Deque without removing it or advancing the view beyond it.
    peekleft(): Looks at the end value of the Deque without removing it or advancing the view before it.
    size(): returns the size of the Deque.
    """

    def __init__(self, iterable=None):
        """Initiate the Deque as an instance of DLL."""
        try:
            self._container = DLL(iterable)
        except TypeError:
            raise TypeError("Need to initialize with an iterable or empty. Otherwise just append/appendleft values.")

    def append(self, val):
        """Add value to the Deque at the end."""
        self._container.push(val)

    def appendleft(self, val):
        """Add value to the Deque at the beginning."""
        self._container.append(val)

    def popleft(self):
        """Remove the first value of the Deque."""
        try:
            return self._container.shift()
        except IndexError:
            raise IndexError("Cannot pop from Empty Deque")

    def pop(self):
        """Remove a value from the end of the deque and returns it (raises an exception if the deque is empty)."""
        try:
            return self._container.pop()
        except IndexError:
            raise IndexError("Cannot pop from Empty Deque")

    def peek(self):
        """Look at next value in the Deque without removing."""
        try:
            return self._container.head.val
        except AttributeError:
            return None

    def peekleft(self):
        """Look at last value in the Deque without removing."""
        try:
            return self._container.tail.val
        except AttributeError:
            return None

    def size(self):
        """How big the Deque is."""
        return self._container.size_of_list
