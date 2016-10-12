"""auto

Revision ID: ad55d401537
Revises: 3db20d7c744c
Create Date: 2014-03-11 12:41:25.052661

"""

# revision identifiers, used by Alembic.
revision = 'ad55d401537'
down_revision = '3db20d7c744c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('radio_program', sa.Column('description', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('radio_program', 'description')
    ### end Alembic commands ###
