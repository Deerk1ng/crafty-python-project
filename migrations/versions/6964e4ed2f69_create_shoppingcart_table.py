"""create shoppingcart table

Revision ID: 6964e4ed2f69
Revises: af599e99ab71
Create Date: 2024-09-12 22:07:09.147404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6964e4ed2f69'
down_revision = 'af599e99ab71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shoppingCart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('total', sa.DECIMAL(), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shoppingCart')
    # ### end Alembic commands ###
