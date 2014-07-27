"""Create funders table

Revision ID: 425a54a5c9dc
Revises: 3fce8157f88
Create Date: 2014-07-23 23:55:33.549580

"""

# revision identifiers, used by Alembic.
revision = '425a54a5c9dc'
down_revision = '3fce8157f88'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'funders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
    )

def downgrade():
    op.drop_table('funders')
