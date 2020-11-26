import pytest

from homework5.task2.print_result import custom_sum


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [(([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]), ((1, 2, 3, 4), 10)],
)
def test_custom_sum_functionality(data, expected_result):

    assert custom_sum(*data) == expected_result


def test_custom_sum_metadata():

    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"


def test_custom_sum_without_decor():
    without_decor = custom_sum.__original_func
    result = without_decor(1, 2, 3, 4)

    assert result == 10
