"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Order:
    def __init__(self, price, dicount_strategy: Strategy = None):
        self.price = price
        self._discount_strategy = dicount_strategy

    @property
    def discount_strategy(self) -> Strategy:
        return self._discount_strategy

    @discount_strategy.setter
    def discount_strategy(self, dicount_strategy: Strategy) -> None:
        self._discount_strategy = dicount_strategy

    def final_price(self) -> int:
        discount = 0
        if self._discount_strategy:
            discount = self._discount_strategy.count_dicount(self)
        return self.price - discount


class Strategy(ABC):
    @abstractmethod
    def count_dicount(self, order: Order):
        pass


class MorningDiscount(Strategy):
    def count_dicount(order: Order) -> int:
        return order.price * 0.25


class ElderDiscount(Strategy):
    def count_dicount(order: Order) -> int:
        return order.price * 0.9


class YourDiscount(Strategy):
    def count_dicount(order: Order) -> int:
        return order.price * (-0.15)
