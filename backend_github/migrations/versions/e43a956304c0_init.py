"""init

Revision ID: e43a956304c0
Revises: 39a44cf8f1c7
Create Date: 2025-03-23 18:38:10.395625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e43a956304c0'
down_revision: Union[str, None] = '39a44cf8f1c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
