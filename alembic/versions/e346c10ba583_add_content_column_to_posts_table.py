"""add content column to posts table

Revision ID: e346c10ba583
Revises: 6acb6375a108
Create Date: 2022-01-10 22:23:32.977767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e346c10ba583'
down_revision = '6acb6375a108'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
