# data-structures

##Linked_List##

###Consists of a series of nodes.###
    
    ####Methods####
    push(val): adds a node at the head, increments size of list.
    pop(): removes the node at the head, deincrements size of list.
    size(): returns size of LinkedList
    search(val): searches list for node containing val and returns that node.
    remove(node_to_delete): takes a node as argument, searches for it, and removes it from list, then deincrements size of list
    display(): returns LinkedList as a stringified tuple-looking object.
    """

12/27/2016

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           59      0   100%
src/test_linked_list.py      75      0   100%
-------------------------------------------------------
TOTAL                       134      0   100%


========================== 30 passed in 0.15 seconds


----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/linked_list.py           59      0   100%
src/test_linked_list.py      75      0   100%
-------------------------------------------------------
TOTAL                       134      0   100%


========================== 30 passed in 0.15 seconds


12/18/2016

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
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


