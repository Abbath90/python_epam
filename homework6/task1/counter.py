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
    setattr(cls, 'counter', 0)

    def __init__(self):
        cls.counter += 1

    def get_created_instances(self):
        return cls.counter

    def reset_created_instances(self):
        last_value = cls.counter
        cls.counter = 0
        return last_value

    setattr(cls, '__init__', __init__)
    setattr(cls, 'get_created_instances', get_created_instances)
    setattr(cls, 'reset_created_instances', reset_created_instances)

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances(None))
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())
    print(user.reset_created_instances())
    print(user.get_created_instances())