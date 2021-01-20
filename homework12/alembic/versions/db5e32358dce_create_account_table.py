"""create account table

Revision ID: db5e32358dce
Revises: 
Create Date: 2021-01-19 17:26:17.577499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db5e32358dce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "student",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
    )

    op.create_table(
        "teacher",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
    )

    op.create_table(
        "homework",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("text", sa.String, nullable=False),
        sa.Column("deadline", sa.String, nullable=False),
        sa.Column("teacher_id", sa.Integer, sa.ForeignKey("teachers.id")),
        sa.Column("created", sa.String, nullable=False),
    )

    op.create_table(
        "homework_result",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("students.id")),
        sa.Column("homework_id", sa.Integer, sa.ForeignKey("homeworks.id")),
        sa.Column("solution", sa.String, nullable=False),
        sa.Column("created", sa.String, nullable=False),
    )



def downgrade():
    op.drop_table("homework_results")
    op.drop_table("homeworks")
    op.drop_table("teachers")
    op.drop_table("students")
