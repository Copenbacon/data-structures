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
        self.size_of_list = 0

    def push(self, val):
        """Insert value to head of the list."""
        if not self.head:
            new_node = Node(val)
            self.head = new_node
            print(self.head)
            self.size_of_list += 1
            return self.head
        else:
            new_node = self.head
            while new_node.next is not None:
                new_node = new_node.next
            newer_node = Node(val)
            new_node.next = newer_node
            print(self.head)
            self.size_of_list += 1
            return self.head

    def pop(self):
        """Remove value from head of list and return it to user."""
        value_popped = self.head.val
        self.head = self.head.next
        self.size_of_list -= 1
        return value_popped

    def size(self):
        """Return the size of the list."""
        return self.size_of_list


    def search(self, val):
        """Return the val of the node when searched."""
        current = self.head
        flag = False
        while current and flag is False:
            if val == current.val:
                flag = True
                return  current
            else:
                current = current.next
        if current ==None:
                return None
