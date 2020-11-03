from typing import List

import pytest
from maxmin.maxmin import find_maximum_and_minimum
from pytest_mock import mocker


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("some_file.txt", (4, -1)),
    ],
)
def test_maxmin(value: str, expected_result: List[int], mocker):
    mocker.patch("maxmin.maxmin.read_file_to_list", return_value=[1, 2, 4, -1])
    actual_result = find_maximum_and_minimum(value)
    assert actual_result == expected_result
