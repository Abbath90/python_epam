from collections.abc import Callable
from typing import Tuple

import pytest

from homework2.task4.cache import cache


@pytest.mark.parametrize(
    ["func", "data", "expected_result"],
    [
        ((lambda x, y: x ** y ** 2), (100, 200), True),
        ((lambda x, y, z: x + y + z), (1, 2, 3), True),
    ],
)
def test_cache(func: Callable, data: Tuple[int], expected_result: bool):
    temp_result = cache(func)
    val_1 = temp_result(*data)
    val_2 = temp_result(*data)
    actual_result = val_1 is val_2

    assert actual_result == expected_result
