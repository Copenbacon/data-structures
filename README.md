# data-structures
##Dec 14, 2016

A singly linked-list might be more appropriate for maintaining some kind of line or queue, like when you have a list of something that goes out in a particular order. FIrst thing that comes to mind is Ticketmaster. You have a set number of tickets in inventory and a lot of people want them. As they hit submit, they are placed in the linked list to maintain their order number. As they receive their ticket, they are removed from the list. I guess you could also use it for some kind of first in, last out operation, but I'm not sure where that would apply.

Doubly linked lists are great for the above as well, but if you want to know where the end of the list is and what is at it, a doubly linked_list is helpful. Not exactly sure of a good use case for this.

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


========================== 84 passed in 0.30 seconds ===========================
py35 inst-nodeps: /media/copenbacon/OS/Users/Conor/codefellows/401/data-structures/.tox/dist/data-structures-0.1.zip
py35 installed: coverage==4.2,data-structures==0.1,decorator==4.0.10,ipython==5.1.0,ipython-genutils==0.1.0,pexpect==4.2.1,pickleshare==0.7.4,prompt-toolkit==1.0.9,ptyprocess==0.5.1,py==1.4.31,Pygments==2.1.3,pytest==3.0.5,pytest-cov==2.4.0,simplegeneric==0.8.1,six==1.10.0,traitlets==4.3.1,wcwidth==0.1.7
py35 runtests: PYTHONHASHSEED='1164392363'
py35 runtests: commands[0] | py.test src --cov=src --cov-report term-missing
============================= test session starts ==============================
platform linux -- Python 3.5.2, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
rootdir: /media/copenbacon/OS/Users/Conor/codefellows/401/data-structures, inifile: 
plugins: cov-2.4.0
collected 84 items 

src/test_dll.py .......................................
src/test_linked_list.py ........................
src/test_stack.py .....................

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


========================== 84 passed in 0.33 seconds ===========================
___________________________________ summary ____________________________________
  py27: commands succeeded
  py35: commands succeeded
  congratulations :)



## Dec 13, 2016
Weird bug, can't figure out. Can run tests multiple times and get different results. Have had all permutations. Had py27 succeed and py3 fail, had vice versa, had both succeed, and had both fail. It has something to do with our test_push_stack test in test_stack.py, but it's only a certain parameter from the PUSH_STACK_TABLE, the dictionaries we pass in. Displaying the dictionaries from the function call will randomly switch keys 1 and 2 from the initial dictionary passed in so that our message will appear with them in some sort of random order.


UPDATE: Above bug fixed. Because Dictionaries are unordered, you cannot predict how they will be iterated over n the hash because we don't (yet) have access to the hash. Changed test to assert str(val) is in the displayed stack/LinkedList

#Test logs:

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


  =================================== FAILURES ===================================
  ___________ test_push_stack[iterable3-val3-({'three': 3},one,two,)] ____________

  iterable = {'one': 1, 'two': 2}, val = {'three': 3}
  result = "({'three': 3},one,two,)"

      @pytest.mark.parametrize("iterable, val, result", PUSH_STACK_TABLE)
      def test_push_stack(iterable, val, result):
          """Test the push method to see entire stack is updated with new value."""
          from stack import Stack
          stack_push = Stack(iterable)
          stack_push.push(val)
  >       assert stack_push._container.display() == result
  E       assert "({'three': 3},two,one,)" == "({'three': 3},one,two,)"
  E         - ({'three': 3},two,one,)
  E         ?                   ----
  E         + ({'three': 3},one,two,)
  E         ?              ++++

  src/test_stack.py:86: AssertionError
  ===================== 1 failed, 38 passed in 0.49 seconds ======================

  src/test_linked_list.py ..................
  src/test_stack.py .....................

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
  ___________________________________ summary ____________________________________
  ERROR:   py27: commands failed
    py35: commands succeeded

    (data-structures) copenbacon @ CopenComp ~/codefellows/401/data-structures (stack)
    └─ $ ▶ tox
    GLOB sdist-make: /media/copenbacon/OS/Users/Conor/codefellows/401/data-structures/setup.py
    py27 inst-nodeps: /media/copenbacon/OS/Users/Conor/codefellows/401/data-structures/.tox/dist/data-structures-0.1.zip
    py27 installed: backports.shutil-get-terminal-size==1.0.0,coverage==4.2,data-structures==0.1,decorator==4.0.10,enum34==1.1.6,ipython==5.1.0,ipython-genutils==0.1.0,pathlib2==2.1.0,pexpect==4.2.1,pickleshare==0.7.4,prompt-toolkit==1.0.9,ptyprocess==0.5.1,py==1.4.31,Pygments==2.1.3,pytest==3.0.5,pytest-cov==2.4.0,simplegeneric==0.8.1,six==1.10.0,traitlets==4.3.1,wcwidth==0.1.7
    py27 runtests: PYTHONHASHSEED='239123734'
    py27 runtests: commands[0] | py.test src --cov=src --cov-report term-missing
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
    rootdir: /media/copenbacon/OS/Users/Conor/codefellows/401/data-structures, inifile: 
    plugins: cov-2.4.0
    collected 39 items 

    src/test_linked_list.py ..................
    src/test_stack.py .....................

    ---------- coverage: platform linux2, python 2.7.12-final-0 ----------
    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    src/linked_list.py           56      1    98%   35
    src/stack.py                 14      0   100%
    src/test_linked_list.py      49      0   100%
    src/test_stack.py            41      0   100%
    -------------------------------------------------------
    TOTAL                       160      1    99%


    ========================== 39 passed in 0.31 seconds ===========================
    py35 inst-nodeps: /media/copenbacon/OS/Users/Conor/codefellows/401/data-structures/.tox/dist/data-structures-0.1.zip
    py35 installed: coverage==4.2,data-structures==0.1,decorator==4.0.10,ipython==5.1.0,ipython-genutils==0.1.0,pexpect==4.2.1,pickleshare==0.7.4,prompt-toolkit==1.0.9,ptyprocess==0.5.1,py==1.4.31,Pygments==2.1.3,pytest==3.0.5,pytest-cov==2.4.0,simplegeneric==0.8.1,six==1.10.0,traitlets==4.3.1,wcwidth==0.1.7
    py35 runtests: PYTHONHASHSEED='239123734'
    py35 runtests: commands[0] | py.test src --cov=src --cov-report term-missing
    ============================= test session starts ==============================
    platform linux -- Python 3.5.2, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
    rootdir: /media/copenbacon/OS/Users/Conor/codefellows/401/data-structures, inifile: 
    plugins: cov-2.4.0
    collected 39 items 

    src/test_linked_list.py ..................
    src/test_stack.py .....................

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
