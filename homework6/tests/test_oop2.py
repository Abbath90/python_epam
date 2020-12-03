import pytest

from homework6.task2.oop_2 import (
    DeadLineException,
    Homework,
    HomeworkResult,
    Student,
    Teacher,
)


@pytest.fixture(scope="module")
def instance_creation_teacher():
    teacher = Teacher("Daniil", "Shadrin")

    return teacher


"""@pytest.fixture(scope='module')
def instance_creation_homework():
    homework = Homework("Learn functions", 0)

    return homework"""


@pytest.fixture(scope="module")
def instance_creation_student():
    student = Student("Roman", "Petrov")

    return student


def test_do_homework(instance_creation_student, instance_creation_teacher):
    homework = instance_creation_teacher.create_homework("Learn OOP", 1)
    result = instance_creation_student.do_homework(homework, "I have done this hw")

    assert isinstance(result, HomeworkResult)


def test_do_homework_with_error(instance_creation_student, instance_creation_teacher):
    homework = instance_creation_teacher.create_homework("Read docs", 0)
    with pytest.raises(DeadLineException, match="You are late"):
        instance_creation_student.do_homework(homework, "I have done this hw")


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [(("Learn functions", 0), False), (("Learn functions", 5), True)],
)
def test_homework_activity(
    instance_creation_teacher, data: Homework, expected_result: bool
):
    homework = instance_creation_teacher.create_homework(*data)
    assert homework.is_active() == expected_result


def test_homework_result_with_error(instance_creation_student):
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(instance_creation_student, "not_a_homework", "solution", 0)


def test_homework_result(instance_creation_student, instance_creation_teacher):
    homework = instance_creation_teacher.create_homework("Read docs", 0)
    homework_result = HomeworkResult(
        instance_creation_student, homework, "I have done this hw", 1
    )
    assert homework_result.author is instance_creation_student
    assert homework_result.homework is homework
    assert homework_result.solution == "I have done this hw"
    assert homework_result.created == 1


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [("I have done this hw", True), ("done", False)],
)
def test_check_homework(
    instance_creation_student,
    instance_creation_teacher,
    data: str,
    expected_result: bool,
):
    homework = instance_creation_teacher.create_homework("Read docs", 5)
    homework_result = HomeworkResult(instance_creation_student, homework, data, 5)
    assert instance_creation_teacher.check_homework(homework_result) is expected_result


def test_reset_all_results(instance_creation_teacher, instance_creation_student):
    homework1 = instance_creation_teacher.create_homework("Read docs", 1)
    homework2 = instance_creation_teacher.create_homework("Read docs 2", 2)
    instance_creation_teacher.check_homework(
        HomeworkResult(instance_creation_student, homework1, "solution", 1)
    )
    instance_creation_teacher.check_homework(
        HomeworkResult(instance_creation_student, homework2, "solution", 2)
    )
    instance_creation_teacher.reset_results()
    assert instance_creation_teacher.homework_done == {}


def test_reset_the_result(instance_creation_teacher, instance_creation_student):
    homework1 = instance_creation_teacher.create_homework("Read docs", 1)
    homework2 = instance_creation_teacher.create_homework("Read docs 2", 2)
    instance_creation_teacher.check_homework(
        HomeworkResult(instance_creation_student, homework1, "solution", 1)
    )
    instance_creation_teacher.check_homework(
        HomeworkResult(instance_creation_student, homework2, "solution", 2)
    )
    instance_creation_teacher.reset_results(homework1)
    assert instance_creation_teacher.homework_done == {homework2: ["solution"]}
