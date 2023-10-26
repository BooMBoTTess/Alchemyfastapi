"""empty message

Revision ID: a8422c3380ed
Revises: a9dfc682b2bb
Create Date: 2023-10-26 20:56:04.215468

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8422c3380ed'
down_revision: Union[str, None] = 'a9dfc682b2bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
