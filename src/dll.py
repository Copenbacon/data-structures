"""This is the module for doubly-linked lists methods."""
from linked_list import LinkedList


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
    """Define the doubly-linked list class.

    push(val): will insert the value ‘val’ at the head of the list
    append(val): will append the value ‘val’ at the tail of the list
    pop(): will pop the first value off the head of the list and return it.
    shift(): will remove the last value from the tail of the list and return it.
    remove(val): will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.
    Special thnaks to Nick for writing the doc string methods explanations.
    """

    def __init__(self, iterable):
        """Initiate the doubly-linked list."""
        self._container = LinkedList(iterable)
        self.tail = None

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
        self.size_of_list -= 1
        return value_popped
