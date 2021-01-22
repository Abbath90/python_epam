import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from homework12.models import Base, Homework, HomeworkResult, Student, Teacher


@pytest.fixture(scope="session")
def engine():
    return create_engine("sqlite:///homework12/db.sqlite")


@pytest.fixture
def dbsession(engine):
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


def test_workable(dbsession):
    teacher = dbsession.query(Teacher).all()
    assert teacher[0].first_name == "Vadilen"
