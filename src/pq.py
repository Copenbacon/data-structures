"""Implement a priority queue."""


class PikaQueue(object):
    """The Priority Queue Class."""

    def __init__(self, vals=[]):
        """Initialize a priority que."""
        self.pq = {}
        if isinstance(vals, list):
            try:
                for pri, data in vals:
                    self.insert(pri, data)
            except ValueError:
                raise TypeError("Input must be a tuple.")
        else:
            raise TypeError("Input must be a list.")

    def insert(self, pri):
        """Insert."""

    def pop(self):
        """Poppin."""

    def peek(self):
        """Peekin."""
