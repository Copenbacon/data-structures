# data-structures

12/18/2016 - Merged in Stack updates nad Linked List Updates

##Dec 14, 2016

A singly linked-list might be more appropriate for maintaining some kind of line or queue, like when you have a list of something that goes out in a particular order. FIrst thing that comes to mind is Ticketmaster. You have a set number of tickets in inventory and a lot of people want them. As they hit submit, they are placed in the linked list to maintain their order number. As they receive their ticket, they are removed from the list. I guess you could also use it for some kind of first in, last out operation, but I'm not sure where that would apply.

Doubly linked lists are great for the above as well, but if you want to know where the end of the list is and what is at it, a doubly linked_list is helpful. Not exactly sure of a good use case for this.


##Doubly Linked List##
  
  ###Methods###
  __init__(): initializes the DLL class and adds a tail, head, and size_of_list attribute. It also checks that the values passed in are iterable.
  push(): Inserts a value to head of the list
  pop(): Remove node from head of list and return it to user.
  append(): Add a tail to the end of the list.
  shift(): Remove node from end of list and return to user.
  def search(self, val): Return the val of the node when searched.
  remove(): Remove the node passed into the parameter.


##Stack##

  ###Methods###
  __init__(): Initiate the Stack as a instance of LinkedList.
  pop(): Remove the top element from stack and returns it.
  push(): Add a value to the top of the stack.
  _size(): Return the length of the stack.
  _is_empty(): Return true if the stack is empty.


##Linked_List##

    
    ####Methods####
    push(val): adds a node at the head, increments size of list.
    pop(): removes the node at the head, deincrements size of list.
    size(): returns size of LinkedList
    search(val): searches list for node containing val and returns that node.
    remove(node_to_delete): takes a node as argument, searches for it, and removes it from list, then deincrements size of list
    display(): returns LinkedList as a stringified tuple-looking object.
    """

##Dec 27, 2016##

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   74      0   100%
src/linked_list.py           59      0   100%
src/stack.py                 15      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       333      0   100%


========================== 90 passed in 0.41 seconds

----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/dll.py                   74      0   100%
src/linked_list.py           59      0   100%
src/stack.py                 15      0   100%
src/test_dll.py              71      0   100%
src/test_linked_list.py      75      0   100%
src/test_stack.py            39      0   100%
-------------------------------------------------------
TOTAL                       333      0   100%


========================== 90 passed in 0.42 seconds



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
=======


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
<<<<<<< HEAD
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

=======
src/linked_list.py           60      0   100%
src/test_linked_list.py      63      0   100%
-------------------------------------------------------
TOTAL                       123      0   100%


================================================= 25 passed in 0.15 seconds

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
