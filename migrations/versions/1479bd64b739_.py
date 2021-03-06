"""empty message

Revision ID: 1479bd64b739
Revises: 53fdccaa7156
Create Date: 2014-11-25 22:50:47.577212

"""

# revision identifiers, used by Alembic.
revision = '1479bd64b739'
down_revision = '53fdccaa7156'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Path', sa.Column('IP', sa.String(length=255), nullable=True))
    op.add_column('Path', sa.Column('Method', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Path', 'Method')
    op.drop_column('Path', 'IP')
    ### end Alembic commands ###
