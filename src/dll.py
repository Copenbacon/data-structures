"""This is the module for doubly-linked lists methods."""
# encoding: utf-8


class DLLNODE(object):
    """Define the doubly-linked list node class.

    __init__(): instantiates an instance of a node with val, next, and prev.
    """

    def __init__(self, val, next=None, prev=None):
        """Initiate the instance of a node."""
        self.val = val
        self.next = next
        self.prev = prev


class DLL(object):
    """Define the doubly-linked list class."""

    def __init__(self, iterable=None):
        """Instantiate LinkedList class."""
        self.tail = None
        self.head = None
        self.size_of_list = 0
        if iterable and hasattr(iterable, "__iter__") or isinstance(iterable, str):
            for value in iterable:
                self.push(value)
        elif iterable:
            raise TypeError
            print("Please submit an iterable when instantiating the list. You can use the push method to add one value at a time.")

    def push(self, val):
        """Insert value to head of the list."""
        new_node = DLLNODE(val, self.head)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head.next = self.head
            self.head = new_node
        self.size_of_list += 1

    def pop(self):
        """Remove value from head of list and return it to user."""
        if self.head is None:
            raise IndexError("Impossible to pop an empty list")
        value_popped = self.head.val
        self.head = self.head.next
        self.head.prev = None
        if self.head is None:
            self.tail = None
        self.size_of_list -= 1
        return value_popped
