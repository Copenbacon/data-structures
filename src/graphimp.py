# -*- coding: utf-8 -*-
"""The Graph Module."""


class Graph(object):
    u"""Class definition for the Graph Object.

    g.nodes():
        return a list of all nodes in the graph
    g.edges():
        return a list of all edges in the graph
    g.add_node(n):
        adds a new node ‘n’ to the graph
    g.add_edge(n1, n2):
        adds a new edge to the graph connecting ‘n1’ and ‘n2’,
        if either n1 or n2 are not already present in the graph,
        they should be added.
    g.del_node(n):
        deletes the node ‘n’ from the graph,
        raises an error if no such node exists
    g.del_edge(n1, n2):
        deletes the edge connecting ‘n1’ and ‘n2’ from the graph,
        raises an error if no such edge exists
    g.has_node(n):
        True if node ‘n’ is contained in the graph, False if not.
    g.neighbors(n):
        returns the list of all nodes connected to ‘n’ by edges,
        raises an error if n is not in g
    g.adjacent(n1, n2):
        returns True if there is an edge connecting n1 and n2,
        False if not, raises an error if either of the supplied nodes
        are not in g
    g.depth_first_traversal(start): 
        Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
    g.breadth_first_traversal(self, start): 
        Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.
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
        if self.nodes() is not []:
            for starting_point in self.nodetionary:
                for ending_point in self.nodetionary[starting_point]:
                    edge_list.append((starting_point, ending_point))
        return edge_list

    def add_node(self, n):
        """Add a new node 'n' to the graph."""
        self.nodetionary.setdefault(n, [])

    def add_edge(self, n1, n2):
        u"""Add a new edge to the graph connecting ‘n1’ and ‘n2’.

        If either n1 or n2 are not already present in the graph,
        they should be added.
        """
        self.nodetionary.setdefault(n1, []).append(n2)
        self.nodetionary.setdefault(n2, [])

    def del_node(self, n):
        u"""Delete the node ‘n’ from the graph.

        Raises an error if no such node exists.
        """
        try:
            del self.nodetionary[n]
            for key in self.nodetionary:
                if n in self.nodetionary[key]:
                    self.nodetionary[key].remove(n)
        except KeyError:
            raise KeyError("Can't delete a node that doesn't exist.")

    def del_edge(self, n1, n2):
        u"""Delete the edge connecting n1 and n2 from the graph.

        Raises an error if no such edge exists.
        """
        if not self.has_node(n1) or not self.has_node(n2):
            raise KeyError("No such node in graph.")
        try:
            self.nodetionary[n1].remove(n2)
        except ValueError:
            raise ValueError("No such edge exists.")

    def has_node(self, n):
        u"""Return True if node in graph."""
        if n in self.nodetionary:
            return True
        return False

    def neighbors(self, n):
        u"""Return the list of all nodes connected to ‘n’ by edges.

        Raises an error if n is not in graph.
        """
        try:
            return list(self.nodetionary[n])
        except KeyError:
            raise KeyError("Node {} is not in the graph".format(n))

    def adjacent(self, n1, n2):
        u"""Return True if there is an edge connecting n1 and n2, False if not.

        Raises an error if either of the supplied nodes are not in graph.
        """
        if n1 in self.nodetionary and n2 in self.nodetionary:
            if n2 in self.nodetionary[n1]:
                return True
            return False
        else:
            raise KeyError("One of the supplied nodes is not in the graph." +
                           "Here is a current list of nodes: " +
                           str(self.nodes()))

    def depth_first_traversal(self, start):
        """Perform a full depth-first traversal of the graph beginning at start.

        Return the full visited path when traversal is complete.
        """
        try:
            stack = [start]
            visited = set()
            return_list = []
            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    stack.extend(self.nodetionary[vertex][::-1])
                    visited.add(vertex)
                    return_list.append(vertex)
        except KeyError:
            raise KeyError(str(start) + " not in graph. Try again.")
        return return_list

    def breadth_first_traversal(self, start):
        """Perform a full breadth-first traversal of the graph, beginning at start.

        Return the full visited path when traversal is complete.
        """
        try:
            visited = set()
            stack = [start]
            return_list = []
            while stack:
                vertex = stack.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    stack.extend(self.nodetionary[vertex])
                    return_list.append(vertex)
        except KeyError:
            raise KeyError(str(start) + " not in graph. Try again.")
        return return_list


if __name__ == "__main__":
    import random
    import timeit
    graph = Graph()
    for i in range(1000):
        graph.add_edge(random.randint(0, 100), random.randint(0, 100))
    x = random.choice(list(graph.nodetionary))

    def time_graph_trav_breadth(graph, x):
        return graph.breadth_first_traversal(x)

    def time_graph_trav_depth(graph, x):
        return graph.depth_first_traversal(x)

    print(timeit.repeat(
        stmt="time_graph_trav_depth(graph, x)",
        setup="from __main__ import time_graph_trav_depth, graph, x",
        number=1000,
        repeat=3
        ))

    print(timeit.repeat(
        stmt="time_graph_trav_breadth(graph, x)",
        setup="from __main__ import time_graph_trav_breadth, graph, x",
        number=1000,
        repeat=3
        ))

    print("Depth Traversal Method: ", time_graph_trav_depth(graph, x))
    print("Breadth Traversal Method: ", time_graph_trav_breadth(graph, x))