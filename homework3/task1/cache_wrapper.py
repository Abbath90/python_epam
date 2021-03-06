"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2'
"""


from collections.abc import Callable
from functools import wraps


def cache(size_limit: int) -> Callable:
    def wrapper(func: Callable):
        counter = 0
        result = None

        @wraps(func)
        def wrapped(*args, **kwargs):
            nonlocal counter, result
            if counter > 0:
                counter -= 1
                return result
            else:
                result = func(*args, **kwargs)
                counter = size_limit
                return result

        return wrapped

    return wrapper
