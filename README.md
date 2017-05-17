# data-structures

```
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py             104     16    85%   73-74, 178-206
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           109      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       936     22    98%


========================== 251 passed in 0.82 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py             104     16    85%   73-74, 178-206
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           109      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       936     16    98%


========================== 252 passed in 0.88 seconds
```

## Graph

  ### Methods
  ```
  nodes(): return a list of all nodes in the graph
  
  edges(): return a list of all edges in the graph with their weights
  
  add_node(n): adds a new node ‘n’ to the graph
  
  add_edge(n1, n2, weight): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added. Also adds a weight to the edge and is displayed as a tuple (connected_node, weight)
  
  del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
  
  del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
  
  has_node(n): True if node ‘n’ is contained in the graph, False if not.
  
  neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
  
  adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
  
  g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.

  g.breadth_first_traversal(self, start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.

  g.djikstras(start, end): Return shortest path (by weight) between two nodes in the graph by using Djikstra's algorithm.

  g.floyd(start, end): Return shortest path (by weight) between two nodes using the Floy-Warshall algorithm.
  
  g.breadth_first_traversal(self, start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.

  ```

## Priority Queue

  ### Methods
  ```
  def __init__(vals=[]): Initialize a priority queue, and insert any values passed in into the Priority Queue. Must pass a list of items. To pass
  
  def insert(item, pri=float(-inf)): Insert an item into the Priority Queue, if no priority specified, -inf will be the priority,
  
  def pop(): Remove a value from the priority queue.
  
  def peek(): Look at next item to be popped in the Priority Queue.
  ```

## Binary Heap

  ### Methods
  ```
  __init__([iterable]): takes an optional iterable object when instantiating the class.
  
  _perc_ip(val): Send the value up the heap as it is pushed in.
  
  push(val): Append a value to the end of the list, increase list size, push the index that is equal to size, up the list.
  
  _perc_down(val): Send a value down the heap if the heap's rules are violated.
  
  _min_child(val): Find and return the smallest child.
  
  pop(): Remove value a head of heap and sort the heap accordingly.
  ```  

## Deque

  It is important to note that the "tail" of our Deques is actually the front of the Deque.

  ### Methods
  ```
  __init__(): initializes the Deque class as a composite of the DLL class.
  
  append(): uses the push method from DLL to add nodes to the end of the Deque.
  
  appendleft(): uses the append method from DLL to add nodes to the start of the Deque.
  
  popleft(): removes a node from the front of the dequeue
  
  pop(): removes a node from the end of the dequeue
  
  peek(): Looks at the front value of the Deque without removing it or advancing the view beyond it.
  
  peekleft(): Looks at the end value of the Deque without removing it or advancing the view before it.
  
  size(): returns the size of the Deque.
  ```

## Queue

  It is important to note that the "tail" of our queue is actually the front of the Queue.

  ### Methods
  ```
  __init__(): initializes the Queue class as a composite of the DLL class.
  
  enqueue(): uses the push method from DLL to add nodes to the end of the Queue.
  
  dequeue(): removes a node from the front of the dequeue
  
  peek(): Looks at the front value of the Queue without removing it or advancing the view beyond it.
  
  size(): returns the size of the Queue.
  ```

## Doubly Linked List
  
  ### Methods
  ```
  __init__(): initializes the DLL class and adds a tail, head, and size_of_list attribute. It also checks that the values passed in are iterable.
  
  push(): Inserts a value to head of the list
  
  pop(): Remove node from head of list and return it to user.
  
  append(): Add a tail to the end of the list.
  
  shift(): Remove node from end of list and return to user.
  
  def search(self, val): Return the val of the node when searched.
  
  remove(): Remove the node passed into the parameter.
  ```

## Stack

  ### Methods
  ```
  __init__(): Initiate the Stack as a instance of LinkedList.
  
  pop(): Remove the top element from stack and returns it.
  
  push(): Add a value to the top of the stack.
  
  _size(): Return the length of the stack.
  
  _is_empty(): Return true if the stack is empty.
  ```

## Linked_List

  ### Methods
  ```
  push(val): adds a node at the head, increments size of list.
  
  pop(): removes the node at the head, deincrements size of list.
  
  size(): returns size of LinkedList
  
  search(val): searches list for node containing val and returns that node.
  
  remove(node_to_delete): takes a node as argument, searches for it, and removes it from list, then deincrements size of list
  
  display(): returns LinkedList as a stringified tuple-looking object.
  ```
