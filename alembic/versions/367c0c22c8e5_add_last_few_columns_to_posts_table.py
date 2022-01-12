"""add last few columns to posts table

Revision ID: 367c0c22c8e5
Revises: 187afec1cd7b
Create Date: 2022-01-11 18:34:12.621643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '367c0c22c8e5'
down_revision = '187afec1cd7b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
