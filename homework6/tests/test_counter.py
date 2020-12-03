import pytest

from homework6.task1.counter import instances_counter


@instances_counter
class User:
    pass


def test_get_created_instances():
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    user.reset_instances_counter()


def test_reset_instances_counter():
    user, _, _ = User(), User(), User()
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0
