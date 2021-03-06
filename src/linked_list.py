"""The Linked List Module Creates a LinkedList."""


class Node(object):
    """Defining Node Class.

    __init__() adds a val property and an optional next property
    """

    def __init__(self, val, next=None):
        """Instantiate Node Class."""
        self.val = val
        self.next = next


class LinkedList(object):
    """Defining class of LinkedList.

    push(val): adds a node at the head, increments size of list.
    pop(): removes the node at the head, deincrements size of list.
    size(): returns size of LinkedList
    search(val): searches list for node containing val and returns that node.
    remove(node_to_delete): takes a node as argument, searches for it, and removes it from list, then deincrements size of list
    display(): returns LinkedList as a stringified tuple-looking object.
    """

    def __init__(self, iterable=None):
        """Instantiate LinkedList class."""
        self.head = None
        self.size_of_list = 0
        if iterable and hasattr(iterable, "__iter__") or isinstance(iterable, str):
            for value in iterable:
                self.push(value)
        elif iterable:
            raise TypeError("Please submit an iterable when instantiating the list. You can use the push method to add one value at a time.")

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
        try:
            current_node = self.search(node_to_delete.val)
        except AttributeError:
            current_node = node_to_delete
        if current_node is None:
            raise ValueError("Node not in list")
        search_node = self.head
        found = False
        while not found:
            if current_node is self.head:
                self.pop()
                break
            elif search_node.next.val == node_to_delete.val:
                search_node.next = current_node.next
                self.size_of_list -= 1
                break
            else:
                search_node = search_node.next

    def display(self):
        """Display the info."""
        message = u"("
        current_node = self.head
        for i in range(self.size_of_list):
            while current_node.next is not None:
                message += "{}, ".format(str(current_node.val))
                current_node = current_node.next
        message += "{})".format(str(current_node.val))
        return message
