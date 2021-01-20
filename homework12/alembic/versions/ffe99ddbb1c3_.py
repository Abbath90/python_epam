"""empty message

Revision ID: ffe99ddbb1c3
Revises: 
Create Date: 2020-12-28 19:45:31.698881

"""
from alembic import op
import sqlalchemy as sa
from homework12.task1.homework_schema import Student, Homework, Teacher, Homework_result
from sqlalchemy.orm import sessionmaker


# revision identifiers, used by Alembic.
revision = 'ffe99ddbb1c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    engine = sa.create_engine('sqlite:///homework4.sqlite', echo=True)
    Session = sessionmaker(bind=engine)

    Homework.__table__.create(bind=engine, checkfirst=True)
    Teacher.__table__.create(bind=engine, checkfirst=True)
    Student.__table__.create(bind=engine, checkfirst=True)
    Homework_result.__table__.create(bind=engine, checkfirst=True)

    session = Session(bind=op.get_bind())

    stud_1 = Student('Vasya', 'Petrov')
    stud_2 = Student('Katya', 'Ivanova')
    teacher_1 = Teacher('Vadilen', 'Hohenzollern')
    teacher_2 = Teacher('Polikarp', 'Starodubov-Kurbsky')
    homework_1 = Homework('Do it')
    homework_2 = Homework('Do it 2')
    homework_result1 = Homework_result('Some shit')
    homework_1.results = [homework_result1]

    session.add(stud_1)
    session.add(stud_2)
    session.add(teacher_1)
    session.add(teacher_2)
    session.add(homework_1)
    session.add(homework_2)
    session.add(homework_result1)

    session.commit()
    session.close()


def downgrade():
    pass
