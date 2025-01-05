"""empty message

Revision ID: bf3ab4f67d96
Revises: 
Create Date: 2025-01-05 01:27:14.028657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf3ab4f67d96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add the 'full_name' column to the 'committee' table
    with op.batch_alter_table('committee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('full_name', sa.String(length=200), nullable=True))


def downgrade():
    # Remove the 'full_name' column from the 'committee' table
    with op.batch_alter_table('committee', schema=None) as batch_op:
        batch_op.drop_column('full_name')
