"""Renaming students to scholars

Revision ID: d9a7a236a81e
Revises: 791279dd0760
Create Date: 2023-12-23 12:36:40.381403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9a7a236a81e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
