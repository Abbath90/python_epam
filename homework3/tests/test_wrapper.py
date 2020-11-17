from typing import List, Tuple

import pytest
import unittest.mock

from homework3.task1.slow_calc import slow_sum


def f():
    return input("? ")


@pytest.mark.parametrize("func, times", [f, 2])
def test_decor_cache(monkeypatch):
    with mock.patch("builtins.input", return_value = int(times)):
        actual_result_1 = f()
        actual_result_2 = f()
        actual_result_3 = f()

    assert actual_result_1 is actual_result_2 is actual_result_3
