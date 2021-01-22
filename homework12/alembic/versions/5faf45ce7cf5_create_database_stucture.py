"""create database stucture

Revision ID: 5faf45ce7cf5
Revises: 
Create Date: 2021-01-22 12:17:43.065120

"""
from alembic import op
import sqlalchemy as sa
from homework12.models import Student, Teacher, Homework, HomeworkResult
from homework12.crud import engine

# revision identifiers, used by Alembic.
revision = '5faf45ce7cf5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    Homework.__table__.create(bind=engine, checkfirst=True)
    Teacher.__table__.create(bind=engine, checkfirst=True)
    Student.__table__.create(bind=engine, checkfirst=True)
    HomeworkResult.__table__.create(bind=engine, checkfirst=True)


def downgrade():
    op.drop_table("homework_results")
    op.drop_table("homeworks")
    op.drop_table("students")
    op.drop_table("teachers")
