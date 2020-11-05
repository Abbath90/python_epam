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


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        min = int(next(fi))
        try:
            max = int(next(fi))
        except StopIteration:
            max = min
        for line in fi:
            next_line = int(line)
            if next_line < min:
                min = next_line
            elif next_line > max:
                max = next_line
        return (max, min)
