from typing import List, Tuple

import pytest

from homework2.task2.major_minor import major_and_minor_elem


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([-1, -1, 2, 2], (-1, -1)),
        ([1], (1, 1)),
        ([0, 1, 2, 0, 1, 2], (0, 0)),
    ],
)
def test_major_and_minor(data: List[int], expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(data)

    assert actual_result == expected_result
