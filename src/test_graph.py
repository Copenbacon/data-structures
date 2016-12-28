"""Testing the Graph module."""
import pytest

ADD_NODE_TABLE = [
    [[1, 2, 3, 7], {1: [], 2: [], 3: [], 7: []}],
    [[1], {1: []}],
    [["test"], {"test": []}],
    [["test", "this", "works"], {"test": [], "this": [], "works": []}]
]

EDGES_TABLE = [
    [[[1, 2]]], [{(1, 2), (2, 1)}],
    [[[1, 2], [3, 2]]], [{(1, 2), (2, 1), (2, 3), (3, 2)}],
    [[[1, 2], [3, 2], [3, 4]], [{(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3)}]],
]

DELETE_TABLE = [
    [[[1, 2]]], 2, [[]],
    [[[1, 2], [3, 2]]], 3, [{(1, 2), (2, 1)}],
    [[[1, 2], [3, 2], [3, 4]], 4, [{(1, 2), (2, 1), (2, 3), (3, 2)}]],
]


@pytest.fixture
def empty_graph():
    """Graph Fixture."""
    from graphimp import Graph
    return Graph()


def test_empty_graph_exists(empty_graph):
    """Make sure the empty graph has an empty nodetionary."""
    assert empty_graph.nodetionary == {}


@pytest.mark.parametrize("vals, result", ADD_NODE_TABLE)
def test_graph_can_contain_values(vals, result, empty_graph):
    """Adding a node should return a nodetionary with values."""
    for val in vals:
        empty_graph.add_node(val)
    assert empty_graph.nodetionary == result


def test_nodes_is_empty_list_on_empty_graph(empty_graph):
    """Calling nodes method on empty graph should return empty list."""
    assert empty_graph.nodes() == []


@pytest.mark.parametrize("vals, result", ADD_NODE_TABLE)
def test_nodes_returns_list_of_keys(vals, result, empty_graph):
    """The nodes() method should return a list of keys from the Nodetionary. (The nodes)."""
    for val in vals:
        empty_graph.add_node(val)
    assert empty_graph.nodes() == vals


def test_edges_empty_when_no_nodes(empty_graph):
    """Edge list should return empty with empty graph."""
    assert empty_graph.edges() == []


@pytest.mark.parametrize("vals, result", EDGES_TABLE)
def test_edges_on_graph(vals, result, empty_graph):
    """Add edges and make sure they list out when calling edges() method."""
    for val in vals:
        empty_graph.add_edge(val[0], val[1])
    assert empty_graph.edges() == result


def test_delete_node_from_empty_graph_raises_error(empty_graph):
    """Deleting a node from an empty graph should raise an error."""
    with pytest.raises(KeyError):
        empty_graph.del_node(4)


@pytest.mark.parametrize("vals_to_add, val_to_delete, result", DELETE_TABLE)
def test_delete_node_deletes_node_and_edges(vals_to_add, val_to_delete, result, empty_graph):
    """Deleting a node should remove the node and any reference to the node as an edge in the graph."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    empty_graph.del_node(val_to_delete)
    assert empty_graph.edges() == result
