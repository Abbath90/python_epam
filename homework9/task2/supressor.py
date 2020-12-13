"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
#>>> with supressor(IndexError):
#...    [][2]
"""

from contextlib import suppress
from contextlib import contextmanager

class ContextManagerException(Exception):
    pass


class Suppressor_as_class:

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        return exctype is not None and issubclass(exctype, self._exceptions)


@contextmanager
def suppressor_as_generator(exception):
    try:
        yield
    except exception:
        pass

with suppressor_as_generator(IndexError):
    print([][2])

with Suppressor_as_class(IndexError):
    print([][2])
