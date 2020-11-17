"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(any_value, *args):
    list_of_value = list(any_value)
    start = list_of_value.index(args[0])
    if len(args) == 1:
        return list_of_value[:start]
    if len(args) == 2:
        finish = list_of_value.index(args[1])
        return list_of_value[start:finish]
    if len(args) == 3:
        finish = list_of_value.index(args[1])
        step = args[2]
        return list_of_value[start:finish:step]
