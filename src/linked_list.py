"""The Linked List Module Creates a LinkedList."""


class LinkedList(object):
    """Defining class of LinkedList."""

    color = 'red'

    def __init__(self, list):
        """Instantiate LinkedList class."""
        self.list = list

    def push(self, val):
        """Insert value to head of the list."""
        self.list.insert(0, val)
        return self.list
