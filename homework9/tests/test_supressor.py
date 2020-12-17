import pytest

from homework9.task2.supressor import Suppressor_as_class, suppressor_as_generator


def test_supressor_as_generator():
    with suppressor_as_generator(IndexError):
        assert [][2]


def test_supressor_as_class():
    with Suppressor_as_class(IndexError):
        assert [][2]
