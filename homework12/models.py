from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)


class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)


class Homework(Base):
    __tablename__ = "homework"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    deadline = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    created = Column(String, nullable=False)


class HomeworkResult(Base):
    __tablename__ = "homework_result"

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("student.id"))
    homework_id = Column("homework_id", Integer, ForeignKey("homework.id"))
    solution = Column(String, nullable=False)
    created = Column(String, nullable=False)
