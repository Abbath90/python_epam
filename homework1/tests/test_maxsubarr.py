from typing import List

import pytest
from homework1.task5.max_subarr import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["list_of_nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 3, 6, 7], 5, 21),
        ([1, 3, -1, -3, 5, 3, 6, 7], 1, 7),
        ([1, 3, -1, -3, 5, 3, 6, 7], 2, 13),
        ([-1, -3, -1, -3, -5, -3, -6, -7], 3, -1),
        ([2, 0], 2, 2),
        ([2, 0], 1, 2),
        ([2], 1, 2),
    ],
)
def test_max_subarr(list_of_nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(list_of_nums, k)

    assert actual_result == expected_result
