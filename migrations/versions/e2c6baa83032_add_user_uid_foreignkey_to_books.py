"""add user_uid foreignkey to books

Revision ID: e2c6baa83032
Revises: 6769130086d9
Create Date: 2024-11-13 13:41:06.067900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel # ADD THIS


# revision identifiers, used by Alembic.
revision: str = 'e2c6baa83032'
down_revision: Union[str, None] = '6769130086d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('user_uid', sa.Uuid(), nullable=True))
    op.create_foreign_key(None, 'books', 'user_accounts', ['user_uid'], ['uid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'user_uid')
    # ### end Alembic commands ###