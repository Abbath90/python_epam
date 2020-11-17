from collections.abc import Sequence

import pytest

from homework1.task2.check_fib import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], None),
        ([0, 1, 1], None),
        ([8, 13, 21], None),
    ],
)
def test_check_fib(data: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
