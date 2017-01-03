# data-structures


##Jan 2, 2016
##Graph-Traversal

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              91     14    85%   164-192
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           103      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       917     20    98%


========================== 249 passed in 0.85 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              91     14    85%   164-192
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           103      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       917     14    98%


========================== 250 passed in 0.84 seconds

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              91     14    85%   164-192
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           103      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       917     20    98%


========================== 249 passed in 0.91 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              91     14    85%   164-192
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           103      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       917     14    98%


========================== 250 passed in 0.94 seconds

##Graph

  ###Methods###
  nodes(): return a list of all nodes in the graph
  edges(): return a list of all edges in the graph
  add_node(n): adds a new node ‘n’ to the graph
  add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
  del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
  del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
  has_node(n): True if node ‘n’ is contained in the graph, False if not.
  neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
  adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
  g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
  g.breadth_first_traversal(self, start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.

  


##Priority Queue

  ###Methods###
  def __init__(vals=[]): Initialize a priority queue, and insert any values passed in into the Priority Queue. Must pass a list of items. To pass
  def insert(item, pri=float(-inf)): Insert an item into the Priority Queue, if no priority specified, -inf will be the priority,
  def pop(): Remove a value from the priority queue.
  def peek(): Look at next item to be popped in the Priority Queue.


##Binary Heap

###Methods###
__init__([iterable]): takes an optional iterable object when instantiating the class.
  _perc_ip(val): Send the value up the heap as it is pushed in.
  push(val): Append a value to the end of the list, increase list size, push the index that is equal to size, up the list.
  _perc_down(val): Send a value down the heap if the heap's rules are violated.
  _min_child(val): Find and return the smallest child.
  pop(): Remove value a head of heap and sort the heap accordingly.
  

##Deque

  It is important to note that the "tail" of our Deques is actually the front of the Deque.

  ###Methods
  __init__(): initializes the Deque class as a composite of the DLL class.
  append(): uses the push method from DLL to add nodes to the end of the Deque.
  appendleft(): uses the append method from DLL to add nodes to the start of the Deque.
  popleft(): removes a node from the front of the dequeue
  pop(): removes a node from the end of the dequeue
  peek(): Looks at the front value of the Deque without removing it or advancing the view beyond it.
  peekleft(): Looks at the end value of the Deque without removing it or advancing the view before it.
  size(): returns the size of the Deque.


##Queue

  It is important to note that the "tail" of our queue is actually the front of the Queue.

  ###Methods
  __init__(): initializes the Queue class as a composite of the DLL class.
  enqueue(): uses the push method from DLL to add nodes to the end of the Queue.
  dequeue(): removes a node from the front of the dequeue
  peek(): Looks at the front value of the Queue without removing it or advancing the view beyond it.
  size(): returns the size of the Queue.


##Doubly Linked List
  
  ###Methods
  __init__(): initializes the DLL class and adds a tail, head, and size_of_list attribute. It also checks that the values passed in are iterable.
  push(): Inserts a value to head of the list
  pop(): Remove node from head of list and return it to user.
  append(): Add a tail to the end of the list.
  shift(): Remove node from end of list and return to user.
  def search(self, val): Return the val of the node when searched.
  remove(): Remove the node passed into the parameter.


##Stack

  ###Methods
  __init__(): Initiate the Stack as a instance of LinkedList.
  pop(): Remove the top element from stack and returns it.
  push(): Add a value to the top of the stack.
  _size(): Return the length of the stack.
  _is_empty(): Return true if the stack is empty.


##Linked_List

    
    ####Methods
    push(val): adds a node at the head, increments size of list.
    pop(): removes the node at the head, deincrements size of list.
    size(): returns size of LinkedList
    search(val): searches list for node containing val and returns that node.
    remove(node_to_delete): takes a node as argument, searches for it, and removes it from list, then deincrements size of list
    display(): returns LinkedList as a stringified tuple-looking object.


##Jan 3, 2017

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              48      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       858      6    99%


========================== 239 passed in 0.72 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              48      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       858      0   100%


========================== 240 passed in 0.85 seconds

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              48      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       858      6    99%


========================== 239 passed in 0.86 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   73      0   100%
src/graphimp.py              48      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       858      0   100%


========================== 240 passed in 0.92 seconds


##Jan 3, 2017


Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/graphimp.py              91     14    85%   164-192
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           103      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       883     20    98%


============================= 233 passed in 0.78 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/graphimp.py              91     14    85%   164-192
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py           103      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       883     14    98%

============================ 234 passed in 0.80 seconds 

##Graph
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/graphimp.py              48      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       824      6    99%

 223 passed in 0.74 seconds

TOTAL                       723      6    99%

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/graphimp.py              48      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       824      0   100%


 224 passed in 0.80 seconds


##Dec 28, 2016##
###Graph###

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/graphimp.py              55      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       831      6    99%


========================== 223 passed in 0.94 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/graphimp.py              55      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py            87      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       831      0   100%


========================== 224 passed in 0.82 seconds



---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      2    95%   34-35
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      4    92%   53-57
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       689      6    99%


========================== 178 passed in 0.67 seconds

src/dll.py                   73      0   100%
src/graphimp.py               0      0   100%
src/linked_list.py           59      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py             0      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       634      0   100%


========================== 175 passed in 0.59 seconds


----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 33      0   100%
src/dll.py                   75      0   100%
src/linked_list.py           59      0   100%
src/pq.py                    41      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_pq.py               48      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       689      0   100%


========================== 179 passed in 0.82 seconds

##Dec 24, 2016 Priority Queue

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 18      0   100%
src/dll.py                   70      0   100%
src/linked_list.py           60      0   100%
src/pq.py                    39      3    92%   5, 36-37
src/queue_.py                12      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            74      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      63      0   100%
src/test_pq.py               45      5    89%   6, 50-54
src/test_queue.py            50      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       637      8    99%


====================================================== 166 passed in 0.54 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 18      0   100%
src/dll.py                   70      0   100%
src/linked_list.py           60      0   100%
src/pq.py                    39      1    97%   7
src/queue_.py                12      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            74      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      63      0   100%
src/test_pq.py               45      1    98%   8
src/test_queue.py            50      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       637      2    99%


====================================================== 167 passed in 0.62 seconds
src/dll.py                   73      0   100%
src/graphimp.py               0      0   100%
src/linked_list.py           59      0   100%
src/queue_.py                18      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py           114      0   100%
src/test_dll.py              71      0   100%
src/test_graph.py             0      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       634      0   100%


========================== 175 passed in 0.65 seconds


##Dec 20, 2016 - Binary Heap

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 18      0   100%
src/dll.py                   70      0   100%
src/linked_list.py           60      0   100%
src/queue_.py                12      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            74      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      63      0   100%
src/test_queue.py            50      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       553      0   100%



========================== 156 passed in 0.50 seconds


----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/binheap.py               47      0   100%
src/deque.py                 18      0   100%
src/dll.py                   70      0   100%
src/linked_list.py           60      0   100%
src/queue_.py                12      0   100%
src/stack.py                 15      0   100%
src/test_binheap.py          34      0   100%
src/test_deque.py            74      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      63      0   100%
src/test_queue.py            50      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       553      0   100%


========================== 156 passed in 0.59 seconds


##Dec 19, 2016 - Deque
12/18/2016 - Merged in Stack updates and Linked List Updates


##Dec 14, 2016

A singly linked-list might be more appropriate for maintaining some kind of line or queue, like when you have a list of something that goes out in a particular order. FIrst thing that comes to mind is Ticketmaster. You have a set number of tickets in inventory and a lot of people want them. As they hit submit, they are placed in the linked list to maintain their order number. As they receive their ticket, they are removed from the list. I guess you could also use it for some kind of first in, last out operation, but I'm not sure where that would apply.

Doubly linked lists are great for the above as well, but if you want to know where the end of the list is and what is at it, a doubly linked_list is helpful. Not exactly sure of a good use case for this.


## 12/30/16

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   75      0   100%
src/linked_list.py           59      0   100%
src/queue.py                 18      0   100%
src/stack.py                 15      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       408      0   100%


========================== 110 passed in 0.49 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   75      0   100%
src/linked_list.py           59      0   100%
src/queue.py                 18      0   100%
src/stack.py                 15      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            56      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       408      0   100%


========================== 110 passed in 0.45 seconds

##Dec 27, 2016

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 33      0   100%
src/dll.py                   74      0   100%
src/linked_list.py           59      0   100%
src/queue.py                 18      0   100%
src/stack.py                 15      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            53      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       515      0   100%


========================== 139 passed in 0.48 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 33      0   100%
src/dll.py                   74      0   100%
src/linked_list.py           59      0   100%
src/queue.py                 18      0   100%
src/stack.py                 15      0   100%
src/test_deque.py            78      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            53      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       515      0   100%


========================== 139 passed in 0.52 seconds

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   74      0   100%
src/linked_list.py           59      0   100%
src/queue.py                 18      0   100%
src/stack.py                 15      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            53      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       404      0   100%


========================== 109 passed in 0.48 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   74      0   100%
src/linked_list.py           59      0   100%
src/queue.py                 18      0   100%
src/stack.py                 15      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_queue.py            53      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       404      0   100%


========================== 109 passed in 0.51 seconds

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 18      0   100%
src/dll.py                   70      0   100%
src/linked_list.py           60      0   100%
src/queue.py                 12      0   100%
src/stack.py                 15      0   100%
src/test_deque.py            74      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      63      0   100%
src/test_queue.py            50      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       472      0   100%


==================================== 131 passed in 0.44 seconds



----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/deque.py                 18      0   100%
src/dll.py                   70      0   100%
src/linked_list.py           60      0   100%
src/queue.py                 12      0   100%
src/stack.py                 15      0   100%
src/test_deque.py            74      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      63      0   100%
src/test_queue.py            50      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       472      0   100%


==================================== 131 passed in 0.52 seconds



---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           59      0   100%
src/stack.py                 15      0   100%
src/test_linked_list.py      75      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       188      0   100%


========================== 51 passed in 0.33 seconds



----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           59      0   100%
src/stack.py                 15      0   100%
src/test_linked_list.py      75      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       188      0   100%


========================== 51 passed in 0.32 seconds 

##Dec 18, 2016 - Merged in DLL, Stack, Linked List Updates

##Dec 15, 2016
Test Coverage at 100% for queue.py

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   70      0   100%
src/linked_list.py           61      6    90%   36, 47, 66-67, 84-85
src/queue.py                 12      0   100%
src/stack.py                 14      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      59      0   100%
src/test_queue.py            50      0   100%
src/test_stack.py            41      0   100%
-------------------------------------------------------
TOTAL                       378      6    98%


----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   70      0   100%
src/linked_list.py           61      6    90%   36, 47, 66-67, 84-85
src/queue.py                 12      0   100%
src/stack.py                 14      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      59      0   100%
src/test_queue.py            50      0   100%
src/test_stack.py            41      0   100%
-------------------------------------------------------
TOTAL                       378      6    98%


  py35: commands succeeded
  congratulations :)


12/18/2016 - Stack updates
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           60      0   100%
src/stack.py                 15      0   100%
src/test_linked_list.py      63      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       177      0   100%


================================================= 46 passed in 0.20 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           60      0   100%
src/stack.py                 15      0   100%
src/test_linked_list.py      63      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       177      0   100%


================================================= 46 passed in 0.22 seconds


         +12/27/2016
 +
 +---------- coverage: platform linux2, python 2.7.12-final-0 ----------
 +Name                      Stmts   Miss  Cover   Missing
 +-------------------------------------------------------
 +src/linked_list.py           59      0   100%
 +src/test_linked_list.py      75      0   100%
 +-------------------------------------------------------
 +TOTAL                       134      0   100%
 +
 +
 +========================== 30 passed in 0.15 seconds
 +
 +
 +----------- coverage: platform linux, python 3.5.2-final-0 -----------
 +Name                      Stmts   Miss  Cover   Missing
 +-------------------------------------------------------
 +src/linked_list.py           59      0   100%
 +src/test_linked_list.py      75      0   100%
 +-------------------------------------------------------
 +TOTAL                       134      0   100%
 +
 +
 +========================== 30 passed in 0.15 seconds


12/18/2016


---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   72      0   100%
src/linked_list.py           61      6    90%   36, 47, 66-67, 84-85
src/stack.py                 14      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      59      0   100%
src/test_stack.py            41      0   100%
-------------------------------------------------------
TOTAL                       318      6    98%


----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   72      0   100%
src/linked_list.py           61      6    90%   36, 47, 66-67, 84-85
src/stack.py                 14      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      59      0   100%
src/test_stack.py            41      0   100%
-------------------------------------------------------
TOTAL                       318      6    98%


----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           60      0   100%
src/test_linked_list.py      63      0   100%
-------------------------------------------------------
TOTAL                       123      0   100%


================================================= 25 passed in 0.15 seconds


## Dec 13, 2016
Weird bug, can't figure out. Can run tests multiple times and get different results. Have had all permutations. Had py27 succeed and py3 fail, had vice versa, had both succeed, and had both fail. It has something to do with our test_push_stack test in test_stack.py, but it's only a certain parameter from the PUSH_STACK_TABLE, the dictionaries we pass in. Displaying the dictionaries from the function call will randomly switch keys 1 and 2 from the initial dictionary passed in so that our message will appear with them in some sort of random order.


UPDATE: Above bug fixed. Because Dictionaries are unordered, you cannot predict how they will be iterated over in the hash because we don't (yet) have access to the hash. Changed test to assert str(val) is in the displayed stack/LinkedList

UPDATED 12/14/16
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           61      6    90%   36, 47, 66-67, 84-85
src/stack.py                 14     14     0%   2-28
src/test_linked_list.py      59      0   100%
-------------------------------------------------------
TOTAL                       134     20    85%


================================ 24 passed in 0.13 seconds =================================

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           61      6    90%   36, 47, 66-67, 84-85
src/stack.py                 14     14     0%   2-28
src/test_linked_list.py      59      0   100%
-------------------------------------------------------
TOTAL                       134     20    85%


================================ 24 passed in 0.14 seconds =================================
_________________________________________ summary __________________________________________
  py27: commands succeeded
  py35: commands succeeded
  congratulations :)



---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           59      2    97%   55-56
src/test_linked_list.py      57      0   100%
-------------------------------------------------------
TOTAL                       116      2    98%


========================== 17 passed in 0.13 seconds ===========================

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           59      2    97%   55-56
src/test_linked_list.py      57      0   100%
-------------------------------------------------------
TOTAL                       116      2    98%


========================== 17 passed in 0.12 seconds ===========================
___________________________________ summary ____________________________________
  py27: commands succeeded
  py35: commands succeeded
  congratulations :)



  ---------- coverage: platform linux2, python 2.7.12-final-0 ----------
  Name                      Stmts   Miss  Cover   Missing
  -------------------------------------------------------
  src/linked_list.py           56      1    98%   35
  src/stack.py                 14      0   100%
  src/test_linked_list.py      49      0   100%
  src/test_stack.py            41      0   100%
  -------------------------------------------------------
  TOTAL                       160      1    99%



  ----------- coverage: platform linux, python 3.5.2-final-0 -----------
  Name                      Stmts   Miss  Cover   Missing
  -------------------------------------------------------
  src/linked_list.py           56      1    98%   35
  src/stack.py                 14      0   100%
  src/test_linked_list.py      49      0   100%
  src/test_stack.py            41      0   100%
  -------------------------------------------------------
  TOTAL                       160      1    99%


  ========================== 39 passed in 0.21 seconds ===========================

    ---------- coverage: platform linux2, python 2.7.12-final-0 ----------
    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    src/linked_list.py           56      1    98%   35
    src/stack.py                 14      0   100%
    src/test_linked_list.py      49      0   100%
    src/test_stack.py            41      0   100%
    -------------------------------------------------------
    TOTAL                       160      1    99%



    ----------- coverage: platform linux, python 3.5.2-final-0 -----------
    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    src/linked_list.py           56      1    98%   35
    src/stack.py                 14      0   100%
    src/test_linked_list.py      49      0   100%
    src/test_stack.py            41      0   100%
    -------------------------------------------------------
    TOTAL                       160      1    99%


    ========================== 39 passed in 0.19 seconds ===========================
    ___________________________________ summary ____________________________________
      py27: commands succeeded
      py35: commands succeeded
      congratulations :)
