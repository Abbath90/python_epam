import pytest

from homework11.task2.discount import (
    ElderDiscount,
    MorningDiscount,
    Order,
    YourDiscount,
)


def test_create_discount_order():
    order = Order(100, MorningDiscount)
    assert order.final_price() == 75


def test_create_order_without_discount():
    order = Order(100)
    assert order.final_price() == 100


def test_change_discount_strategy_in_order():
    order = Order(100, ElderDiscount)
    order.discount_strategy = YourDiscount
    assert order.final_price() == 115
