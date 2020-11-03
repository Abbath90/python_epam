from typing import List

import pytest
from max_subarr.max_subarr import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["list_of_nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-1, -3, -1, -3, -5, -3, -6, -7], 3, -5),
        ([2, 0], 2, 2),
        ([2, 0], 1, 2),
        ([2], 1, 2),
    ],
)
def test_max_subarr(list_of_nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(list_of_nums, k)

    assert actual_result == expected_result
