"""empty message

Revision ID: b6951c2c2091
Revises: c156ac0ea9fa
Create Date: 2023-05-04 14:34:25.681745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6951c2c2091'
down_revision = 'c156ac0ea9fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('completed_at', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('description', sa.String(), nullable=False))
    op.add_column('task', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'title')
    op.drop_column('task', 'description')
    op.drop_column('task', 'completed_at')
    # ### end Alembic commands ###