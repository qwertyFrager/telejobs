"""delete role

Revision ID: 7c9e967dd136
Revises: 0bba777db934
Create Date: 2025-03-23 18:47:19.137777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c9e967dd136'
down_revision: Union[str, None] = '0bba777db934'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_role_key', 'users', type_='unique')
    op.drop_column('users', 'role')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_role_key', 'users', ['role'])
    # ### end Alembic commands ###
