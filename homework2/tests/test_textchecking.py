from typing import Dict, List, Tuple

import pytest

from homework2.task1.text_checking import text_checking


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (
            "./homework2/tests/test_stuff/data.txt",
            (
                [
                    "rückständig",
                    "schlagworte",
                    "schwerpunkt",
                    "moralischen",
                    "zukünftiges",
                    "landstriche",
                    "praktischen",
                    "erstaunlich",
                    "verständlich",
                    "kalyptischen",
                ],
                "›",
                5391,
                2972,
                "ä",
            ),
        ),
    ],
)
def test_text_checking(
    data: str, expected_result: Tuple[List[str], str, int, int, str]
):
    actual_result = text_checking(data)
зк
    assert actual_result == expected_result
