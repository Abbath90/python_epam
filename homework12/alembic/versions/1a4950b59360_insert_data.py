"""insert data

Revision ID: 1a4950b59360
Revises: 5faf45ce7cf5
Create Date: 2021-01-22 12:27:51.399639

"""
from alembic import op
import sqlalchemy as sa
import datetime as dt
from homework12.models import Student, Teacher, Homework, HomeworkResult
from homework12.crud import Session

# revision identifiers, used by Alembic.
revision = '1a4950b59360'
down_revision = '5faf45ce7cf5'
branch_labels = None
depends_on = None


def upgrade():
    session = Session(bind=op.get_bind())
    objects = [
        Student(first_name="Vova", last_name="Petrov"),
        Student(first_name="Kolya", last_name="Ivanov"),
        Teacher(first_name="Vadilen", last_name="Hohenzollern"),
        Homework(text="Do it!", deadline=f"{dt.timedelta(days=5)}", teacher_id=1, created=f"{dt.datetime.now()}"),
        HomeworkResult(author_id=1, homework_id=1, solution="My Solution", created=f"{dt.datetime.now()}"),
    ]
    session.add_all(objects)
    session.commit()
    session.close()


def downgrade():
    op.execute("DELETE FROM student")
    op.execute("DELETE FROM teacher")
    op.execute("DELETE FROM homework_result")
    op.execute("DELETE FROM homework")

