from typing import List, Tuple

import pytest

from homework3.task1.cache_wrapper import f


def test_decor_cache(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: 1)
    actual_result_1 = f()
    actual_result_2 = f()
    actual_result_3 = f()

    assert actual_result_1 is actual_result_2 is actual_result_3
