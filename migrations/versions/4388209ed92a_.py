"""empty message

Revision ID: 4388209ed92a
Revises: f90d43fd18cc
Create Date: 2022-11-07 11:19:34.875058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4388209ed92a'
down_revision = 'f90d43fd18cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('trash', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'trash')
    # ### end Alembic commands ###
