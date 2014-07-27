"""Create tags table

Revision ID: 2a51dc98ea0e
Revises: 425a54a5c9dc
Create Date: 2014-07-24 00:00:59.607487

"""

# revision identifiers, used by Alembic.
revision = '2a51dc98ea0e'
down_revision = '425a54a5c9dc'

from alembic import op
import sqlalchemy as sa
import settings as db


def upgrade():
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('tags')
