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


def cache(size_limit=0):
    def decorator(func):
        input_cache = {}
        counter = 0

        @wraps(func)
        def wrapper(*args):
            nonlocal counter
            if args in input_cache and size_limit > counter:
                counter += 1
                return input_cache[args]
            else:
                input_cache.clear()
                counter = 0
                result = func(*args)
                input_cache[args] = result
                return result

        return wrapper

    return decorator


@cache(size_limit=2)
def f():
    return input("? ")
