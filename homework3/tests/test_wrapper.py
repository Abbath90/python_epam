from homework3.task1.cache_wrapper import cache
from io import StringIO


@cache(size_limit=2)
def f():
    return input()


def test_decor_cache(monkeypatch):
    mock_input_str = StringIO("1")
    monkeypatch.setattr("sys.stdin", mock_input_str)
    actual_result_1 = f()
    actual_result_2 = f()
    actual_result_3 = f()

    assert actual_result_1 is actual_result_2 is actual_result_3
