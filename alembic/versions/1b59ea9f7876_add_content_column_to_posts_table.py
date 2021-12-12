"""add content column to posts table

Revision ID: 1b59ea9f7876
Revises: a5dcd55faa42
Create Date: 2021-12-11 14:28:34.636731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b59ea9f7876'
down_revision = 'a5dcd55faa42'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
