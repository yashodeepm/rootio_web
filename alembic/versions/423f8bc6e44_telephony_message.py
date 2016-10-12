"""telephony_message

Revision ID: 423f8bc6e44
Revises: 15d91338011f
Create Date: 2016-08-25 14:52:01.309909

"""

# revision identifiers, used by Alembic.
revision = '423f8bc6e44'
down_revision = '15d91338011f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'telephony_call', sa.Column('duration', sa.Integer(), nullable=True))
    op.drop_column(u'telephony_call', u'end_time')
    op.add_column(u'telephony_message', sa.Column('from_phonenumber', sa.String(length=20), nullable=True))
    op.add_column(u'telephony_message', sa.Column('to_phonenumber', sa.String(length=20), nullable=True))
    op.drop_column(u'telephony_message', u'from_phonenumber_id')
    op.drop_column(u'telephony_message', u'to_phonenumber_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'telephony_message', sa.Column(u'to_phonenumber_id', sa.INTEGER(), nullable=True))
    op.add_column(u'telephony_message', sa.Column(u'from_phonenumber_id', sa.INTEGER(), nullable=True))
    op.drop_column(u'telephony_message', 'to_phonenumber')
    op.drop_column(u'telephony_message', 'from_phonenumber')
    op.add_column(u'telephony_call', sa.Column(u'end_time', postgresql.TIMESTAMP(), nullable=True))
    op.drop_column(u'telephony_call', 'duration')
    ### end Alembic commands ###
