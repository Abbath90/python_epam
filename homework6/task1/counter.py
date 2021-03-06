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
    orig_init = cls.__init__

    def __init__(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        cls.counter += 1

    @classmethod
    def get_created_instances(cls):
        return cls.counter

    @classmethod
    def reset_instances_counter(cls):
        last_value = cls.counter
        cls.counter = 0
        return last_value

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls
