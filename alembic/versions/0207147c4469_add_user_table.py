"""add user table

Revision ID: 0207147c4469
Revises: 1b59ea9f7876
Create Date: 2021-12-11 14:50:02.762659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0207147c4469'
down_revision = '1b59ea9f7876'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
