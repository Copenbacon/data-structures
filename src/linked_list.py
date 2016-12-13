"""The Linked List Module Creates a LinkedList."""


class Node(object):
    """Defining Node Class."""

    def __init__(self, val, next=None):
        """Instantiate Node Class."""
        self.val = val
        self.next = next


class LinkedList(object):
    """Defining class of LinkedList."""

    def __init__(self, iterable=None):
        """Instantiate LinkedList class."""
        self.head = None
        self.size_of_list = 0
        if iterable and hasattr(iterable, "__iter__") or isinstance(iterable, str):
            for value in iterable:
                self.push(value)
        elif iterable:
            self.push(iterable)

    def push(self, val):
        """Insert value to head of the list."""
        new_node = Node(val, self.head)
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

    def size(self):
        """Return the size of the list."""
        return self.size_of_list

    def search(self, val):
        """Return the val of the node when searched."""
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next

    def remove(self, node_to_delete):
        """Remove the node passed into the parameter."""
        current_node = self.search(node_to_delete)
        found = False
        print(self.size_of_list, "Old Size of List")
        previous = self.head
        search_node = self.head.next
        while search_node and found is False:
            if current_node is self.head:
                self.pop()
                found = True
            elif current_node.val == node_to_delete:
                previous.next = current_node.next
                found = True
        self.size_of_list -= 1
        print(self.size_of_list, "New Size of List")
        return previous.next

    def display(self):
        """Display the info."""
        message = u"("
        current_node = self.head
        for i in range(self.size_of_list):
            message += "{}, ".format(str(current_node.val))
            current_node = current_node.next
        message += ")"
        return message
