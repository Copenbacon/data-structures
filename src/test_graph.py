"""Testing the Graph module."""
import pytest

ADD_NODE_TABLE = [
    [[1, 2, 3, 7], {1: [], 2: [], 3: [], 7: []}],
    [[1], {1: []}],
    [["test"], {"test": []}],
    [["test", "this", "works"], {"test": [], "this": [], "works": []}]
]

EDGES_TABLE = [
    [[[1, 2]], [(1, 2)]],
    [[[1, 2], [3, 2]], [(1, 2), (3, 2)]],
    [[[1, 2], [3, 2], [3, 4]], [(1, 2), (3, 2), (3, 4)]],
]

DELETE_TABLE = [
    [[[1, 2]], 2, []],
    [[[1, 2], [3, 2]], 3, [(1, 2)]],
    [[[1, 4], [3, 2], [3, 4]], 4, [(3, 2)]],
]

DELETE_EDGES_TABLE = [
    [[[1, 2]], [1, 3]],
    [[[1, 2], [3, 2]], [4, 1]],
]

DELETE_EDGES_TABLE2 = [
    [[[1, 2], [3, 2]], [1, 3]],
    [[[1, 2], [3, 2], [4, 3], [4, 2]], [4, 1]],
]

DELETE_EDGES_TABLE3 = [
    [[[1, 2], [3, 2]], [1, 2], 1],
    [[[1, 2], [3, 2], [4, 3], [4, 2]], [4, 3], 3],
]

DELETE_EDGES_TABLE4 = [
    [[[1, 2], [3, 2]], [1, 2], [(3, 2)]],
    [[[1, 2], [3, 2], [4, 3], [4, 2]], [4, 3], [(1, 2), (3, 2), (4, 2)]],
]

HAS_NODE_TABLE = [
    [[1], 3, False],
    [[1, 3], 3, True],
    [[1, 2, 3, 4], 5, False],
    [[1, 2, 3, 4, 5], 5, True],
]

NEIGHBORS_TABLE = [
    [[[1, 2], [3, 2]], 1, [2]],
    [[[1, 2], [3, 2], [1, 3]], 1, [2, 3]],
    [[[1, 2], [3, 2], [1, 3]], 2, []],
    [[[1, 2], [3, 2], [1, 3], [3, 4], [4, 1]], 1, [2, 3]],
]

NEIGHBORS_TABLE2 = [
    [[[1, 2], [3, 2]], 4],
    [[[1, 2], [3, 2], [1, 3]], 7],
    [[[1, 2], [3, 2], [1, 3]], 5],
    [[[1, 2], [3, 2], [1, 3], [3, 4], [4, 1]], 8],
]

ADJACENCY_TABLE = [
    [[[1, 2], [2, 1]], (1, 2), True],
    [[[1, 2], [3, 2]], (3, 1), False],
    [[[1, 2], [3, 2], [2, 3], [2, 1]], (2, 1), True],
    [[[1, 2], [3, 2], [1, 3], [3, 4], [4, 1]], (2, 4), False]
]

BREADTH_TRAVERSAL_TABLE = [
    [[[1, 2], [2, 3], [3, 4]], 1, [1, 2, 3, 4]],
    [[[1, 3], [2, 4], [4, 3], [2, 5]], 2, [2, 4, 5, 3]],
    [[[1, 2], [2, 3], [3, 4], [3, 2], [3, 1], [2, 1]], 2, [2, 3, 1, 4]],
]

DEPTH_TRAVERSAL_TABLE = [
    [[[1, 2], [2, 3], [3, 4]], 1, [1, 2, 3, 4]],
    [[[1, 2], [2, 3], [3, 4]], 2, [2, 3, 4]],
    [[[1, 2], [2, 3], [3, 4]], 3, [3, 4]],
    [[[1, 2], [2, 3], [3, 4], [3, 2], [3, 1], [2, 1]], 3, [3, 4, 2, 1]],
    [[[1, 3], [2, 4], [4, 3], [2, 5]], 2, [2, 4, 3, 5]]
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
    assert len(empty_graph.nodes()) == len(vals)


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


def test_delete_edges_from_empty_graph_raise_error(empty_graph):
    """Deleting edges that don't exist shouldraise an error."""
    with pytest.raises(KeyError):
        empty_graph.del_edge(4, 6)


@pytest.mark.parametrize("vals_to_add, edges_to_delete", DELETE_EDGES_TABLE)
def test_delete_edges_when_node_not_in_graph_raise_keyerror(vals_to_add, edges_to_delete, empty_graph):
    """Deleting nodes that don't exist should raise an error."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    with pytest.raises(KeyError):
        empty_graph.del_edge(edges_to_delete[0], edges_to_delete[1])


@pytest.mark.parametrize("vals_to_add, edges_to_delete", DELETE_EDGES_TABLE2)
def test_delete_edges_not_in_graph_raise_valerror(vals_to_add, edges_to_delete, empty_graph):
    """Deleting edges that don't exist shouldraise an error."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    with pytest.raises(ValueError):
        empty_graph.del_edge(edges_to_delete[0], edges_to_delete[1])


@pytest.mark.parametrize("vals_to_add, edges_to_delete, result", DELETE_EDGES_TABLE3)
def test_delete_edges_deletes_edges(vals_to_add, edges_to_delete, result, empty_graph):
    """Deleting edges should render a list that has the length we expect."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    empty_graph.del_edge(edges_to_delete[0], edges_to_delete[1])
    assert len(empty_graph.edges()) == result


@pytest.mark.parametrize("vals_to_add, edges_to_delete, result", DELETE_EDGES_TABLE4)
def test_delete_edges_deletes_edges_and_edges_method_reflects_that(vals_to_add, edges_to_delete, result, empty_graph):
    """Deleting edges and calling the edges() method should render a list of the edges."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    empty_graph.del_edge(edges_to_delete[0], edges_to_delete[1])
    assert empty_graph.edges() == result


@pytest.mark.parametrize("nodes_to_add, node_to_test, result", HAS_NODE_TABLE)
def test_has_node(nodes_to_add, node_to_test, result, empty_graph):
    """If node is in graph, return true, else false."""
    for node in nodes_to_add:
        empty_graph.add_node(node)
    assert empty_graph.has_node(node_to_test) == result


def test_one_node_in_list_has_no_neighbors(empty_graph):
    """A one node list should have no neighbors."""
    empty_graph.add_node(1)
    assert empty_graph.neighbors(1) == []


@pytest.mark.parametrize("vals_to_add, node_to_test, result", NEIGHBORS_TABLE)
def test_has_neighbors(vals_to_add, node_to_test, result, empty_graph):
    """If node is in graph, return neighbors."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    assert empty_graph.neighbors(node_to_test) == result


@pytest.mark.parametrize("vals_to_add, node_to_test", NEIGHBORS_TABLE2)
def test_has_neighbors_raises_error_when_node_not_in_graph(vals_to_add, node_to_test, empty_graph):
    """If node is not in graph, return error."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    with pytest.raises(KeyError):
        empty_graph.neighbors(node_to_test)


def test_adjacency_raise_error_when_node_not_present(empty_graph):
    """Testing adjacency on an unpresent node should raise KeyError."""
    with pytest.raises(KeyError):
        empty_graph.adjacent(1, 2)


@pytest.mark.parametrize("vals_to_add, vals_to_test, result", ADJACENCY_TABLE)
def test_adjacency_works_as_expected(vals_to_add, vals_to_test, result, empty_graph):
    """Return True if nodes are adjacent, false if not."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    assert empty_graph.adjacent(vals_to_test[0], vals_to_test[1]) == result


def test_empty_graph_traversal_return_breadth(empty_graph):
    """Return Key Error because value not in graph."""
    with pytest.raises(KeyError):
        empty_graph.breadth_first_traversal(1)


def test_empty_graph_traversal_return_deptth(empty_graph):
    """Return Key Error because value not in graph."""
    with pytest.raises(KeyError):
        empty_graph.depth_first_traversal(1)


@pytest.mark.parametrize("vals_to_add, val_to_test, result", DEPTH_TRAVERSAL_TABLE)
def test_depth_traversal_works(vals_to_add, val_to_test, result, empty_graph):
    """Result should happen based on val passed in. Depth Table."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    assert empty_graph.depth_first_traversal(val_to_test) == result


@pytest.mark.parametrize("vals_to_add, val_to_test, result", BREADTH_TRAVERSAL_TABLE)
def test_breadth_traversal_works(
    vals_to_add,
    val_to_test,
    result,
    empty_graph):
    """Result should happen based on val passed in. Depth Table."""
    for val in vals_to_add:
        empty_graph.add_edge(val[0], val[1])
    assert empty_graph.breadth_first_traversal(val_to_test) == result
