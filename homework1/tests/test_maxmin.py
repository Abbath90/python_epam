import os.path
from typing import Tuple

import pytest
from task3.maxmin import find_maximum_and_minimum

path_to_test_stuff = "./homework1/tests/test_stuff/"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (os.path.join(path_to_test_stuff, "test_file_maxmin_1.txt"), (100, -100)),
        (os.path.join(path_to_test_stuff, "test_file_maxmin_2.txt"), (3, 1)),
        (os.path.join(path_to_test_stuff, "test_file_maxmin_3.txt"), (2, 1)),
        (os.path.join(path_to_test_stuff, "test_file_maxmin_4.txt"), (1, 1)),
    ],
)
def test_maxmin(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result


# ./homework1/tests/test_stuff/test_file_maxmin_4.txt
"""@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("some_file.txt", (4, -1)),
    ],
)
def test_maxmin(value: str, expected_result: List[int], mocker):
    mocker.patch("task3.maxmin.read_file_to_list", return_value=[1, 2, 4, -1])
    actual_result = find_maximum_and_minimum(value)
    assert actual_result == expected_result"""
