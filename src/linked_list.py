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
        if self.head is None:
            self.head = Node(val)
            print(self.head)
            self.size_of_list += 1
            return self.head
        else:
            self.head = Node(val, self.head)
            print(self.head)
            self.size_of_list += 1
            return self.head

    def pop(self):
        """Remove value from head of list and return it to user."""
        self.head = self.head.next
        self.size_of_list -= 1
        value_popped = self.head.val
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
                return current
            else:
                current = current.next
        if current is None:
                return None

    def remove(self, node_to_delete):
        """Remove the node passed into the parameter."""
        node = self.search(node_to_delete)
        print(self.size_of_list, "Old Size of List")
        if node is self.head:
            return self.pop()
        current = self.head
        while current.val and current.next is not None:
                current.next = current.next.next
                current = current.next
        self.size_of_list -= 1
        print(self.size_of_list, "New Size of List")
        return current
