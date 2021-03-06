"""add phone number

Revision ID: 63830c5ca388
Revises: 1cbe5b2c1d6b
Create Date: 2022-01-11 19:14:24.411935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63830c5ca388'
down_revision = '1cbe5b2c1d6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
