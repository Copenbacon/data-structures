"""Implement a priority queue."""

inf = float("inf")


class PikaQ(object):
    """The Priority Queue Class.

    def __init__(vals=None): Initialize a priority queue, and insert any values passed in into the Priority Queue. Must pass a list of items.
    def insert(item, pri=float(-inf)): Insert an item into the Priority Queue, if no priority specified, -inf will be the priority,
    def pop(): Remove the highest priority value from the priority queue.
    def peek(): Look at next item to be popped in the Priority Queue.


    """

    def __init__(self, vals=None):
        """Initialize a priority queue."""
        if vals is None:
            vals = []
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
        """Insert an item into the Priority Queue according to its priority."""
        item = (val, pri)
        if type(item[1]) is str or hasattr(type(item[1]), "__iter__") or type(item[1]) is bool:
            raise TypeError("Priority must be a number.")
        if item[1] in self.pq:
            self.pq[item[1]].append(item[0])
        else:
            self.pq[item[1]] = [item[0]]

    def pop(self):
        """Remove the highest priority value from the priority queue and return it."""
        try:
            poppin_key = min(self.pq.keys())
            poppin_list = self.pq[poppin_key]
            val_popped = poppin_list[0]
            self.pq[poppin_key].remove(poppin_list[0])
        except ValueError:
            raise IndexError("Empty PikaQ is un-poppable.")
        if len(poppin_list) == 0:
            self.pq.pop(poppin_key)
        return val_popped

    def peek(self):
        """Look at next item to be popped in the Priority Queue."""
        if len(self.pq) > 0:
            return str(min(self.pq)) + ": " + str(self.pq[min(self.pq)][0])
        else:
            return
