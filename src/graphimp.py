# -*- coding: utf-8 -*-
"""The Graph Module."""


class Graph(object):
    u"""Class definition for the Graph Object.

    g.nodes(): return a list of all nodes in the graph
    g.edges(): return a list of all edges in the graph
    g.add_node(n): adds a new node ‘n’ to the graph
    g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
    g.del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
    g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
    g.has_node(n): True if node ‘n’ is contained in the graph, False if not.
    g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
    g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
    """

    def __init__(self):
        """Instantiation of the Graph."""
        self.nodetionary = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.nodetionary)

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for starting_point in self.nodetionary:
            for ending_point in starting_point:
                edge_list.append((starting_point, ending_point))
        return set(edge_list)

    def add_node(self, n):
        """Add a new node 'n' to the graph."""
        self.nodetionary.setdefault(n, [])

    def add_edge(self, n1, n2):
        u"""Add a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added."""
        try:
            self.nodetionary[n1].append(n2)
        except KeyError:
            self.nodetionary.setdefault(n1, n2)
        try:
            self.nodetionary[n2].append(n1)
        except KeyError:
            self.nodetionary.setdefault(n2, n1)

    def del_node(self, n):
        u"""Delete the node ‘n’ from the graph, raises an error if no such node exists."""
        try:
            del self.nodetionary[n]
            for key in self.nodetionary:
                if n in self.nodetionary[key]:
                    self.nodetionary[key].remove(n)
        except KeyError:
            raise KeyError("Can't delete a node that doesn't exist.")

    def del_edge(self, n1, n2):
        u"""Delete the edge connecting n1 and n2 from the graph, raises an error if no such edge exists."""
        try:
            self.nodetionary[n1].remove(n2)
        except ValueError:
            raise ValueError("No such edge exists.")
        except KeyError:
            raise KeyError("No such node in graph.")
        try:
            self.nodetionary[n2].remove(n1)
        except ValueError:
            raise ValueError("No such edge exists.")
        except KeyError:
            raise KeyError("No such node in graph.")

    def has_node(self, n):
        u"""Return True if node in graph."""
        if n in self.nodetionary:
            return True
        return False

    def neighbors(self, n):
        u"""Return the list of all nodes connected to ‘n’ by edges, raises an error if n is not in graph."""
        try:
            return list(self.nodetionary[n])
        except KeyError:
            raise KeyError("Node {} is not in the graph".format(n))

    def adjacent(self, n1, n2):
        u"""Return True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in graph."""
        if n1 in self.nodetionary and n2 in self.nodetionary:
            if n1 in self.nodetionary[n2] and n2 in self.nodetionary[n1]:
                return True
            return False
        else:
            raise KeyError("One of the supplied nodes is not in the graph. Here is a current list of nodes:" + self.nodes())
