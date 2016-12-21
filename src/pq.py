"""Implement a priority queue."""


class PikaQueue(object):
    """The Priority Queue Class."""

    def __init__(self, vals=[]):
        """Initialize a priority que."""
        self.pq = {}
        if isinstance(vals, list):
            try:
                for val in vals:
                    self.insert(val)
            except ValueError:
                raise TypeError("Input must be a tuple.")
        else:
            raise TypeError("Input must be a list.")

    def insert(self, item):
        """Insert."""
        if type(item[0]) is not int:
            raise TypeError("Priority must be a number.")
        if item[0] in self.pq:
            self.pq[item[0]].append(item[1])
        else:
            self.pq[item[0]] = [item[1]]

    def pop(self):
        """Poppin."""

    def peek(self):
        """Peekin."""
