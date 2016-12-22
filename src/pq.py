"""Implement a priority queue."""


from math import inf


class PikaQ(object):
    """The Priority Queue Class."""

    def __init__(self, vals=[]):
        """Initialize a priority que."""
        self.pq = {}
        if hasattr(vals, "__iter__"):
            try:
                for val, pri in vals:
                    self.insert(val, pri)
            except TypeError:
                for val in vals:
                    self.insert(val)
            except ValueError:
                print("Too many values inserted in one of your lists")
        elif not hasattr(type(vals, "__iter__")):
            self.insert(vals)
        else:
            raise ValueError("Need to submit either a single value, a list of values, or a list of values tupled/listed with priorities.")

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
        poppin_key = min(self.pq.keys())
        poppin_list = self.pq[poppin_key]
        self.pq[poppin_key].remove(poppin_list[0])
        if len(self.pq) == 0:
            raise IndexError("Empty PikaQ is un-poppable.")
        if len(poppin_list) == 0:
            self.pq.pop(poppin_key)

    def peek(self):
        """Peekin."""
