import pytest

from homework5.task1.courses import Homework, Student, Teacher


def test_student_init():
    student = Student("Roman", "Petrov")

    assert student.last_name == "Petrov"


def test_teacher_init():
    teacher = Teacher("Daniil", "Shadrin")

    assert teacher.last_name == "Shadrin"


def test_homework_init():
    homework = Homework("Learn functions", 0)

    assert homework.text == "Learn functions"


@pytest.mark.parametrize(["data", "expected_result"], [(("Learn functions", 0), None)])
def test_homework_expirity(data: Homework, expected_result: bool):
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    homework = teacher.create_homework(*data)
    assert student.do_homework(homework) is expected_result


@pytest.mark.parametrize("data", [Homework("Learn functions", 5)])
def test_do_homework(data: Homework):
    student = Student("Roman", "Petrov")
    assert student.do_homework(data) is data


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [(("Learn functions", 0), False), (("Learn functions", 5), True)],
)
def test_homework_activity(data: Homework, expected_result: bool):
    homework = Homework(*data)
    assert homework.is_active() == expected_result
