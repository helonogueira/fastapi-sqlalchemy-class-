"""Create loans table

Revision ID: 6d0f25acf01f
Revises: 603338f23cc1
Create Date: 2026-05-07 19:19:33.763685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d0f25acf01f'
down_revision: Union[str, None] = '603338f23cc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('loans',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('book_id', sa.Integer(), sa.ForeignKey('books.id'), nullable=True),
        sa.Column('user_name', sa.String(), nullable=True),
        sa.Column('loan_date', sa.Date(), nullable=True),
        sa.Column('return_date', sa.Date(), nullable=True),
        sa.Column('returned', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_loans_id', 'loans', ['id'], unique=False)
    op.create_index('ix_loans_user_name', 'loans', ['user_name'], unique=False)

def downgrade() -> None:
    op.drop_index('ix_loans_user_name', table_name='loans')
    op.drop_index('ix_loans_id', table_name='loans')
    op.drop_table('loans')
    # ### end Alembic commands ###
