"""name

Revision ID: ba180186d52e
Revises: d9a7a236a81e
Create Date: 2023-12-23 13:02:05.297294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba180186d52e'
down_revision = 'd9a7a236a81e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='title')
    pass


def downgrade() -> None:
    pass
