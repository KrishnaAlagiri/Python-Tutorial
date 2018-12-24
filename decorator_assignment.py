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
def logged(func):
    def inside(*args, **kwargs):
        print("you called ",func.__name__,*kwargs,args)
        print("it returned",func(*args))
    return inside

@logged
def func(*args):
    return 3 + len(args)

@logged
def add(a,b):
    return(a+b)

func(4, 4, 4)
add(5,3)
