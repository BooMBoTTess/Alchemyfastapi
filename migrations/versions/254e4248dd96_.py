"""empty message

Revision ID: 254e4248dd96
Revises: a8422c3380ed
Create Date: 2023-10-26 21:00:30.656064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '254e4248dd96'
down_revision: Union[str, None] = 'a8422c3380ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
