import pytest

from homework9.task2.supressor import SuppressorAsClass, suppressor_as_generator


def test_supressor_as_generator():
    with suppressor_as_generator(IndexError):
        assert [][2]


def test_supressor_as_class():
    with SuppressorAsClass(IndexError):
        assert [][2]
