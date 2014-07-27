"""Create funder_tags table

Revision ID: 58488055b524
Revises: 37a9a8d81a29
Create Date: 2014-07-24 00:15:41.441503

"""

# revision identifiers, used by Alembic.
revision = '58488055b524'
down_revision = '37a9a8d81a29'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'funder_tags',
        sa.Column('funder_id', sa.Integer, sa.ForeignKey('funders.id')),
        sa.Column('tag_id', sa.Integer, sa.ForeignKey('tags.id')),
    )


def downgrade():
    op.drop_table('funder_tags')
