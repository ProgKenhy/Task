"""schedules is_continuous delete

Revision ID: 4380549935fa
Revises: 28e4850b3c98
Create Date: 2025-03-18 17:24:21.446182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4380549935fa'
down_revision: Union[str, None] = '28e4850b3c98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schedules', 'is_continuous')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedules', sa.Column('is_continuous', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
