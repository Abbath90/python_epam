"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    input_cache = {}

    def cache_func(*args):
        if args in input_cache:
            return input_cache[args]
        else:
            result = func(*args)
            input_cache[args] = result
            return result

    return cache_func
