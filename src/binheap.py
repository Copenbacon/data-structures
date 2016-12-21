"""Implement a binary heap. Special thanks to https://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html for inspiration."""


class BBinnyHeap(object):
    """The Binary Heap Class.

    __init__([iterable]): takes an optional iterable object when instantiating the class.
    _perc_ip(val): Send the value up the heap as it is pushed in.
    push(val): Append a value to the end of the list, increase list size, push the index that is equal to size, up the list.
    _perc_down(val): Send a value down the heap if the heap's rules are violated.
    _min_child(val): Find and return the smallest child.
    pop(): Remove value a head of heap and sort the heap accordingly.
    """

    def __init__(self, iterable=None):
        """Take an optional iterable object when instantiating the class. Initialize size to zero."""
        self.list_heap = []
        self.size = 0
        if iterable:
            for val in iterable:
                self.push(val)

    def _perc_up(self, val):
        """Send the value up the heap as it is pushed in."""
        while val // 2 > 0:
            if self.list_heap[val] < self.list_heap[val // 2]:
                temp = self.list_heap[val // 2]
                self.list_heap[val // 2] = self.list_heap[val]
                self.list_heap[val] = temp
            val = val // 2

    def push(self, val):
        """Append a value to the end of the list, increase list size, push the index that is equal to size, up the list."""
        if type(val) is list or type(val) is dict or type(val) is tuple:
            raise TypeError("Don't try to push lists, initialize with a list. Did you not plan this out? #trollpy")
        else:
            self.list_heap.insert(0, 0)
            self.list_heap.append(val)
            self.size += 1
            self._perc_up(self.size)
            self.list_heap.remove(0)

    def _perc_down(self, val):
        """Send a value down the heap if the heap's rules are violated."""
        while (val * 2) <= self.size:
            min_child = self._min_child(val)
            if self.list_heap[val] > self.list_heap[min_child]:
                temp = self.list_heap[val]
                self.list_heap[val] = self.list_heap[min_child]
                self.list_heap[min_child] = temp
            val = min_child

    def _min_child(self, val):
        """Find and return the smallest child."""
        if val * 2 + 1 > self.size:
            return val * 2
        else:
            if self.list_heap[val * 2] < self.list_heap[val * 2 + 1]:
                return val * 2
            else:
                return val * 2 + 1

    def pop(self):
        """Remove value a head of heap and sort the heap accordingly."""
        if self.list_heap == []:
            raise IndexError("Cannot pop from empty heap!")
        else:
            self.list_heap.insert(0, 0)
            val = self.list_heap[1]
            self.list_heap[1] = self.list_heap[self.size]
            self.size -= 1
            self.list_heap.pop()
            self._perc_down(1)
            self.list_heap.remove(0)
            return val
