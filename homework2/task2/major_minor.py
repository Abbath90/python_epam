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
from collections import defaultdict


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    dict_of_elems = defaultdict(int)
    for i in inp:
        dict_of_elems[i] += 1
    major_value = max(dict_of_elems, key=dict_of_elems.get)
    minor_value = min(dict_of_elems, key=dict_of_elems.get)
    return (major_value, minor_value)
