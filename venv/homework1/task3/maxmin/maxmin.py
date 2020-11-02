from typing import Tuple, List


def read_file_to_list(file_name: str) -> List[int]:
    list_from_file = []
    with open(file_name) as fi:
        for line in fi:
            list_from_file.append(int(line))
    return list_from_file


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    list_from_file = read_file_to_list(file_name)
    return (max(list_from_file), min(list_from_file))


