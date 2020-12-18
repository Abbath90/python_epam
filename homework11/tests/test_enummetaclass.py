import pytest


from homework11.task1.enum_metaclass import SimplifiedEnum

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_attribute_in_enum():
    assert ColorsEnum.RED == 'RED'


def test_attribute_not_in_enum():
    with pytest.raises(AttributeError, match='YELLOW'):
        ColorsEnum.YELLOW


def test_enum_iteration():
    iterator_form_simplifiedenum = iter(ColorsEnum)
    assert next(iterator_form_simplifiedenum) == 'BLUE'


def test_enum_len():
    assert len(ColorsEnum) == 4

