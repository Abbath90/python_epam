"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import Dict, List, Tuple


def get_key_by_value(inp_dic: Dict, value: int):
    for i in inp_dic.items():
        if i[1] == value:
            return i[0]


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    dict_of_elems = {}
    for i in inp:
        dict_of_elems[i] = dict_of_elems.get(i, 0)
        dict_of_elems[i] += 1
    list_of_values = list(dict_of_elems.values())
    major_value = get_key_by_value(dict_of_elems, max(list_of_values))
    minor_value = get_key_by_value(dict_of_elems, min(list_of_values))
    return (major_value, minor_value)
