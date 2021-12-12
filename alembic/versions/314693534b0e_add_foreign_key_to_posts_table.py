"""add foreign-key to posts table

Revision ID: 314693534b0e
Revises: 0207147c4469
Create Date: 2021-12-11 15:14:14.288394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '314693534b0e'
down_revision = '0207147c4469'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts",
                          referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
