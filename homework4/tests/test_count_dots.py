import pytest
import requests_mock


from homework4.task2.count_dots import count_dots_on_i






@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("ping limit", 3),
        ("pong lomot", 0),
        ("", 0),
    ],
)
def test_count_dots(requests_mock, data: str, expected_result: int):
    requests_mock.get('mock://test.com', text=data)
    actual_result = count_dots_on_i('mock://test.com')

    assert actual_result == expected_result