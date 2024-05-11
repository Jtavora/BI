"""empty message

Revision ID: 9100a9065667
Revises: 4162b08eac98
Create Date: 2024-05-11 16:23:21.032819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9100a9065667'
down_revision: Union[str, None] = '4162b08eac98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
