"""User models

Revision ID: 19e938c88969
Revises: e492c9bee23f
Create Date: 2024-07-01 13:11:33.608130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19e938c88969'
down_revision = 'e492c9bee23f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
