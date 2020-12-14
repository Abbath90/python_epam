"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    level_values = tree.values()
    for level in level_values:
        if isinstance(level, dict):
            counter += find_occurrences(level, element)
        elif isinstance(level, list):
            for sublevel in level:
                if isinstance(sublevel, dict):
                    counter += find_occurrences(sublevel, element)
                elif sublevel == element:
                    counter += 1
        elif level == element:
            counter += 1
    return counter
