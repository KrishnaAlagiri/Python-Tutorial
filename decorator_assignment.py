"""
   Decorators Assignment
==============================
* Write a python program decorator_assignment.py having a decorator "logged" which wraps functions to log function arguments and the return value on each call.
* Provide support for both positional and named arguments (your wrapper function should take both *args and **kwargs and print them both):

    >>> @logged
    ... def func(*args):
    ... return 3 + len(args)
    >>> func(4, 4, 4)
    you called func(4, 4, 4)
    it returned 6
    6

"""
