from typing import List

import pytest

from homework2.task1.text_checking import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (
            "./homework2/tests/test_stuff/data.txt",
            [
                "erquickt",
                "wichtigsten",
                "gewünschten",
                "monopolistisch",
                "darzustellen",
                "leidenschaftlich",
                "beschäftigen",
                "fingerabdrucks",
                "friedensabstimmung",
                "unmißverständliche",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(data: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(data)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("./homework2/tests/test_stuff/data.txt", "›"),
    ],
)
def test_get_rarest_char(data: str, expected_result: str):
    actual_result = get_rarest_char(data)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("./homework2/tests/test_stuff/data.txt", 5391),
    ],
)
def test_count_punctuation_chars(data: str, expected_result: int):
    actual_result = count_punctuation_chars(data)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("./homework2/tests/test_stuff/data.txt", 2972),
    ],
)
def test_count_non_ascii_chars(data: str, expected_result: int):
    actual_result = count_non_ascii_chars(data)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ("./homework2/tests/test_stuff/data.txt", "ä"),
    ],
)
def test_get_most_common_non_ascii_char(data: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(data)

    assert actual_result == expected_result
