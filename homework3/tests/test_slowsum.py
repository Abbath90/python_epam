from time import perf_counter

import pytest

from homework3.task2.slow_calc import slow_sum


@pytest.mark.parametrize("maxtime", [60])
def test_decor_cache(time_setpoint):
    time1 = perf_counter()
    slow_sum()
    time2 = perf_counter()

    assert time2 - time1 < maxtime
