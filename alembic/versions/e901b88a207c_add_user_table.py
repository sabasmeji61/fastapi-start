"""add user table

Revision ID: e901b88a207c
Revises: e346c10ba583
Create Date: 2022-01-10 22:32:38.893731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e901b88a207c'
down_revision = 'e346c10ba583'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
