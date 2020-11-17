from typing import List

import pytest

from homework2.task3.combo import combinations


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        (
            ([1, 2, 3], [4, 6], [7, 8, 9]),
            [
                [1, 4, 7],
                [1, 4, 8],
                [1, 4, 9],
                [1, 6, 7],
                [1, 6, 8],
                [1, 6, 9],
                [2, 4, 7],
                [2, 4, 8],
                [2, 4, 9],
                [2, 6, 7],
                [2, 6, 8],
                [2, 6, 9],
                [3, 4, 7],
                [3, 4, 8],
                [3, 4, 9],
                [3, 6, 7],
                [3, 6, 8],
                [3, 6, 9],
            ],
        ),
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
        (([1], [3]), [[1, 3]]),
    ],
)
def test_combo(args, expected_result: List[int]):
    actual_result = combinations(*args)

    assert actual_result == expected_result
