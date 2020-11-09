from typing import List

import pytest

from homework1.task4.check_sum import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([0, 2, 4], [6, 8, 10], [-6, -10, -12], [0, -16, -18], 6),
        ([0], [0], [0], [0], 1),
        ([1], [1], [-1], [-1], 1),
        ([1], [1], [1], [1], 0),
        ([], [], [], [], 0),
    ],
)
def test_check_sum(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
