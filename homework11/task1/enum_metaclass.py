"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""

from enum import EnumMeta, Enum

class SimplifiedEnum(type):
    def __new__(cls, name, bases, class_dict):
        class_instance = super().__new__(cls, name, bases, class_dict)
        for class_dict_key in class_dict.keys():
            if hasattr(class_dict[class_dict_key], '__iter__'):
                cls.key_attr_name = class_dict_key
        setattr(class_instance, cls.key_attr_name, class_dict[cls.key_attr_name])

        return class_instance

    def __getattr__(cls, key):
        if key in cls.__dict__[cls.key_attr_name]:
            return key
        raise AttributeError(key)

    def __iter__(cls):
        return iter(cls.__dict__[cls.key_attr_name])

    def __len__(cls):
        return len(cls.__dict__[cls.key_attr_name])

