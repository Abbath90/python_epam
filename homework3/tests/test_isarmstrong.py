from typing import List, Tuple

import pytest

from homework3.task4.is_armstrong import is_armstrong


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (9, True),
        (153, True),
        (4679307774, True),
        (423423, False),
    ],
)
def test_is_armstrong(data: List[int], expected_result: Tuple[int, int]):
    actual_result = is_armstrong(data)

    assert actual_result == expected_result
