"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    output_list = [[]]
    for another_list in args:
        temp_list = []
        for input_list in output_list:
            for elem in another_list:
                temp_list.append(input_list + [elem])
        output_list = temp_list
    return output_list
