from typing import List
import pytest

from maxmin.maxmin import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("some_file_1.txt", [4, -1]),
        ("some_file_1.txt", [4, -1]),
        ("some_file_1.txt", [4, -1]),
    ],
)
def test_maxmin(value: str, expected_result: List[int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
