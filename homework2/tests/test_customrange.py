from collections.abc import Sequence
from string import ascii_lowercase
from typing import List, Tuple

import pytest

from homework2.task5.custom_range import custom_range


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ((ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        ((ascii_lowercase, "g", "p"), ["g", "h", "i", "j", "k", "l", "m", "n", "o"]),
        ((ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
        (
            ([1, object(), None, 1, False, [4, 3], range(1, 5)], range(1, 5), None, -1),
            [range(1, 5), [4, 3], False, 1],
        ),
    ],
)
def test_customrange(data: Sequence[any], expected_result: List[any]):
    actual_result = custom_range(*data)

    assert actual_result == expected_result
