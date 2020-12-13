"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
#>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator

#def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    list_of_numbers = []
    for file in file_list:
        with open(file) as file_object:
            for line in file_object.readlines():
                list_of_numbers.append(int(line))

    return(iter(sorted(list_of_numbers)))

it = merge_sorted_files(['1.txt', '2.txt'])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))