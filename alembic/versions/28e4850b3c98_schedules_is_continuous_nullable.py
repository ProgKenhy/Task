"""schedules is_continuous nullable

Revision ID: 28e4850b3c98
Revises: e68cccdf443f
Create Date: 2025-03-17 15:37:19.875276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28e4850b3c98'
down_revision: Union[str, None] = 'e68cccdf443f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedules', 'is_continuous',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedules', 'is_continuous',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
