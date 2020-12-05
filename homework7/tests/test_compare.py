from typing import Tuple

import pytest

from homework7.task2.compare import backspace_compare


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (("ab#c", "ad#c"), True),
        (("a##c", "#a#c"), True),
        (("a#c", "b"), False),
        (("", ""), True),
        (("1", ""), False),
        (("#", "#"), True),
        (("1#", ""), True),
    ],
)
def test_backspace_compare(data: Tuple, expected_result: bool):
    assert backspace_compare(*data) is expected_result
