"""Implement a priority queue."""
import sys

if sys.version_info[0] == 3:
    from math import inf
else:
    inf = float("inf")


class PikaQ(object):
    """The Priority Queue Class.

    def __init__(vals=[]): Initialize a priority queue, and insert any values passed in into the Priority Queue. Must pass a list of items. To pass
    def insert(item, pri=float(-inf)): Insert an item into the Priority Queue, if no priority specified, -inf will be the priority,
    def pop(): Remove a value from the priority queue.
    def peek(): Look at next item to be popped in the Priority Queue.


    """

    def __init__(self, vals=[]):
        """Initialize a priority queue."""
        self.pq = {}
        if not hasattr(vals, "__iter__"):
            self.insert(vals)
        elif hasattr(vals, "__iter__"):
            if any(isinstance(item, dict) for item in vals):
                self.insert(vals)
            else:
                try:
                    for val, pri in vals:
                        self.insert(val, pri)
                except TypeError:
                    for val in vals:
                        self.insert(val)
                except ValueError:
                    raise ValueError("Submitting a string? Put it in a list or tuple first, and give it a priority! Otherwise it will be placed in the highest priority group.")

    def insert(self, val, pri=float(-inf)):
        """Insert an item into the Priority Queue."""
        item = (val, pri)
        if type(item[1]) is str or hasattr(type(item[1]), "__iter__") or type(item[1]) is bool:
            raise TypeError("Priority must be a number.")
        if item[1] in self.pq:
            self.pq[item[1]].append(item[0])
        else:
            self.pq[item[1]] = [item[0]]

    def pop(self):
        """Remove a value from the prioritya queue."""
        if len(self.pq) == 0:
            raise IndexError("Empty PikaQ is un-poppable.")
        poppin_key = min(self.pq.keys())
        poppin_list = self.pq[poppin_key]
        self.pq[poppin_key].remove(poppin_list[0])
        if len(poppin_list) == 0:
            self.pq.pop(poppin_key)

    def peek(self):
        """Look at next item to be popped in the Priority Queue."""
        if len(self.pq) > 0:
            return str(min(self.pq)) + ": " + str(self.pq[min(self.pq)][0])
        else:
            return "Nothing, Priority Q is empty!"
