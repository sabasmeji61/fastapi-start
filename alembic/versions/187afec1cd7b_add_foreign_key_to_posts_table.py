"""add foreign-key to posts table

Revision ID: 187afec1cd7b
Revises: e901b88a207c
Create Date: 2022-01-11 15:41:27.286385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '187afec1cd7b'
down_revision = 'e901b88a207c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
