"""Implement a priority queue."""


from math import inf


class PikaQ(object):
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

    def insert(self, item, pri=float(-inf)):
        """Insert."""
        item = (item, pri)
        if type(item[1]) is str or hasattr(type(item[1]), "__iter__") or type(item[1]) is bool:
            raise TypeError("Priority must be a number.")
        if item[1] in self.pq:
            self.pq[item[1]].append(item[0])
        else:
            self.pq[item[1]] = [item[0]]

    def pop(self):
        """Poppin."""

    def peek(self):
        """Peekin."""
