"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""

from typing import List, Tuple


def sort_short_list(list: List[int]) -> List[int]:
    if len(list) > 1 and (list[0] < list[1]):
        list[0], list[1] = list[1], list[0]
    if len(list) > 2 and (list[1] < list[2]):
        list[1], list[2] = list[2], list[1]
        if list[0] < list[1]:
            list[0], list[1] = list[1], list[0]
    return list


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    list_from_file = []
    with open(file_name) as fi:
        for line in fi:
            list_from_file.append(int(line))
            list_from_file = sort_short_list(list_from_file)
            if len(list_from_file) == 3:
                list_from_file = list_from_file[::2]
    if len(list_from_file) == 1:
        list_from_file.append(list_from_file[0])
    return tuple(list_from_file)
