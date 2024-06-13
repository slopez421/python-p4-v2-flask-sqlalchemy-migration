"""add Department

Revision ID: 13202d924929
Revises: 0e36967f4b1f
Create Date: 2024-06-13 16:15:02.081655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13202d924929'
down_revision = '0e36967f4b1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###