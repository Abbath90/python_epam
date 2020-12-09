import pathlib

import pytest

from homework8.task2.president_db import TableData


def test_get_length():
    with TableData(
        "./homework8/tests/test_stuff/example.sqlite", "presidents"
    ) as president:
        assert len(president) == 3


def test_get_row():
    with TableData(
        "./homework8/tests/test_stuff/example.sqlite", "presidents"
    ) as president:
        assert president["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains():
    with TableData(
        "./homework8/tests/test_stuff/example.sqlite", "presidents"
    ) as president:
        assert "Yeltsin" in president


def test_iterable():
    with TableData(
        "./homework8/tests/test_stuff/example.sqlite", "presidents"
    ) as president:
        assert [i["name"] for i in president] == ["Yeltsin", "Trump", "Big Man Tyrone"]


"""def test_test():
    with TableData('./homework8/tests/test_stuff/example.sqlite', "presidents") as president:
        assert len(president) == 3
        assert president["Yeltsin"] == ('Yeltsin', 999, 'Russia')
        assert "Yeltsin" in president
        assert [i["name"] for i in president] == ["Yeltsin", "Trump", "Big Man Tyrone"]"""
