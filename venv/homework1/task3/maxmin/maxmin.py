from typing import Tuple

file_path = "some_file.txt"

def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    list_from_file = []
    with open(file_name) as fi:
        for line in fi:
            list_from_file.append(int(line))
    return (max(list_from_file), min(list_from_file))

print(find_maximum_and_minimum(file_path))

