from typing import Tuple

import pytest
from task3.maxmin import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("./homework1/tests/test_stuff/test_file_maxmin_1.txt", (100, -100)),
        ("./homework1/tests/test_stuff/test_file_maxmin_2.txt", (3, 1)),
        ("./homework1/tests/test_stuff/test_file_maxmin_3.txt", (2, 1)),
        ("./homework1/tests/test_stuff/test_file_maxmin_4.txt", (1, 1)),
    ],
)
def test_maxmin(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result


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
