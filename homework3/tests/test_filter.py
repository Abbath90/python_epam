from typing import Dict, List

import pytest

from homework3.task3.filter import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly",
    },
]


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ({"type": "person", "name": "Bill"}, [sample_data[0]]),
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
    ],
)
def test_make_filter(value: Dict[any, any], expected_result: List[any]):
    actual_result = make_filter(**value).apply(sample_data)
    assert actual_result == expected_result
