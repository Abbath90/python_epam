import pathlib

import pytest

from homework8.task2.president_db import TableData


@pytest.fixture(scope="module")
def setup_database():
    with TableData(
        "./homework8/tests/test_stuff/example.sqlite", "presidents"
    ) as president:
        yield president


def test_get_length(setup_database):

    assert len(setup_database) == 3


def test_get_row(setup_database):
    assert setup_database["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains(setup_database):
    assert "Yeltsin" in setup_database


def test_iterable(setup_database):
    assert [i["name"] for i in setup_database] == ["Yeltsin", "Trump", "Big Man Tyrone"]
