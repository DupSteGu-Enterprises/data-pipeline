"""create politician table

Revision ID: 3fce8157f88
Revises: None
Create Date: 2014-07-21 20:35:59.570082

"""

# revision identifiers, used by Alembic.
revision = '3fce8157f88'
down_revision = None

from alembic import op
import sqlalchemy as sa
from settings import db_settings as db


def upgrade():
    op.create_table(
        db.POLITICIAN_TABLE,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
    )

def downgrade():
    op.drop_table(db.POLITICIAN_TABLE)
