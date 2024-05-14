"""First_migration

Revision ID: 82b4a144973c
Revises: 8bcc5fa26eb0
Create Date: 2024-05-13 21:24:48.565703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82b4a144973c'
down_revision: Union[str, None] = '8bcc5fa26eb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
