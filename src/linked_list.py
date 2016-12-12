"""The Linked List Module Creates a LinkedList."""


class Node(object):
    """Defining Node Class."""

    def __init__(self, val, next=None):
        """Instantiate Node Class."""
        self.val = val
        self.next = next


class LinkedList(object):
    """Defining class of LinkedList."""

    def __init__(self):
        """Instantiate LinkedList class."""
        self.head = None
        self.size = 0

    def push(self, val):
        """Insert value to head of the list."""
        if not self.head:
            new_node = Node(val)
            self.head = new_node
            return
        else:
            new_node = self.head
            while new_node.next is not None:
                new_node = new_node.next
            newer_node = Node(val)
            new_node.next = newer_node
            return
