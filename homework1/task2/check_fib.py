"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections.abc import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    assert len(data) >= 3
    l = len(data)
    for i, j in enumerate(data):
        if i == l - 2:
            return None
        if not _check_window(data[i], data[i + 1], data[i + 2]):
            raise ValueError("Invalid data")
