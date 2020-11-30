"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""

from functools import wraps

def instances_counter(cls):
    def dec(cls):
        setattr(cls, 'c', 0)  # add atr counter to CLS

        def __init__(self):
            cls.c += 1  # +1 to CLS, not self!

        def get_c(self=None):
            return cls.c  # get current value from CLS

        setattr(cls, '__init__', __init__)  # add new __init__ IT WILL OVERWRITE original __init__
        setattr(cls, 'get_c', get_c)  # add new method
        return cls



@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3