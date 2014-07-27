"""Create politician_funders table

Revision ID: 37a9a8d81a29
Revises: 2a51dc98ea0e
Create Date: 2014-07-24 00:05:35.489770

"""

# revision identifiers, used by Alembic.
revision = '37a9a8d81a29'
down_revision = '2a51dc98ea0e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'politician_funders',
        sa.Column('politician_id', sa.Integer, sa.ForeignKey('politicians.id')),
        sa.Column('funder_id', sa.Integer, sa.ForeignKey('funders.id')),
    )


def downgrade():
    op.drop_table('politician_funders')
