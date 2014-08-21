"""Create contributions table

Revision ID: 11d37bf78cb3
Revises: 58488055b524
Create Date: 2014-08-10 14:12:32.165864

"""

# revision identifiers, used by Alembic.
revision = '11d37bf78cb3'
down_revision = '58488055b524'

from alembic import op
import sqlalchemy as sa
from settings import db_settings as db


def upgrade():
    op.create_table(
        db.CONTRIBUTION_TABLE,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.Date),
        sa.Column('politician_id', sa.Integer, sa.ForeignKey('politicians.id')),
        sa.Column('funder_id', sa.Integer, sa.ForeignKey('funders.id')),
    )


def downgrade():
    op.drop_table(db.CONTRIBUTION_TABLE)
