"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    setattr(cls, "counter", 0)

    __class__ = cls

    def __init__(self):
        super().__init__()
        cls.counter += 1

    def get_created_instances(self):
        return cls.counter

    def reset_instances_counter(self):
        last_value = cls.counter
        cls.counter = 0
        return last_value

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls


@instances_counter
class User:
    pass

