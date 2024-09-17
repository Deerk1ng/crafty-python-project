"""empty message

Revision ID: 44150366419e
Revises:
Create Date: 2024-09-13 22:09:05.149244

"""
from alembic import op
import sqlalchemy as sa
import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '44150366419e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('shop_name', sa.String(length=40), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('shop_name'),
    sa.UniqueConstraint('username')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE orders SET SCHEMA {SCHEMA};")
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ownerId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['ownerId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE products SET SCHEMA {SCHEMA};")
    # op.create_table('shoppingCarts',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('userId', sa.Integer(), nullable=False),
    # sa.Column('total', sa.Float(), nullable=False),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    # sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # if environment == "production":
    #     op.execute(f"ALTER TABLE shoppingCarts SET SCHEMA {SCHEMA};")
    # op.create_table('cartItems',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('cartId', sa.Integer(), nullable=False),
    # sa.Column('productId', sa.Integer(), nullable=False),
    # sa.Column('quantity', sa.Integer(), nullable=False),
    # sa.Column('createdAt', sa.DateTime(), nullable=False),
    # sa.Column('updatedAt', sa.DateTime(), nullable=False),
    # sa.ForeignKeyConstraint(['cartId'], ['shoppingCarts.id'], ),
    # sa.ForeignKeyConstraint(['productId'], ['products.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # if environment == "production":
    #     op.execute(f"ALTER TABLE cartItems SET SCHEMA {SCHEMA};")
    # op.create_table('favorites',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('userId', sa.Integer(), nullable=False),
    # sa.Column('productId', sa.Integer(), nullable=False),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    # sa.ForeignKeyConstraint(['productId'], ['products.id'], ),
    # sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # if environment == "production":
    #     op.execute(f"ALTER TABLE favorites SET SCHEMA {SCHEMA};")
    # op.create_table('orderItems',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('orderId', sa.Integer(), nullable=False),
    # sa.Column('productId', sa.Integer(), nullable=False),
    # sa.Column('quantity', sa.Integer(), nullable=False),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    # sa.ForeignKeyConstraint(['orderId'], ['orders.id'], ),
    # sa.ForeignKeyConstraint(['productId'], ['products.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # if environment == "production":
    #     op.execute(f"ALTER TABLE orderItems SET SCHEMA {SCHEMA};")
    # op.create_table('productImages',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('url', sa.String(length=255), nullable=False),
    # sa.Column('preview', sa.Boolean(), nullable=True),
    # sa.Column('productId', sa.Integer(), nullable=False),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    # sa.ForeignKeyConstraint(['productId'], ['products.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # if environment == "production":
    #     op.execute(f"ALTER TABLE productImages SET SCHEMA {SCHEMA};")
    # op.create_table('reviews',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('userId', sa.Integer(), nullable=False),
    # sa.Column('productId', sa.Integer(), nullable=False),
    # sa.Column('itemRating', sa.Integer(), nullable=False),
    # sa.Column('shippingRating', sa.Integer(), nullable=False),
    # sa.Column('description', sa.Text(), nullable=True),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    # sa.ForeignKeyConstraint(['productId'], ['products.id'], ),
    # sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # if environment == "production":
    #     op.execute(f"ALTER TABLE reviews SET SCHEMA {SCHEMA};")
    # op.create_table('reviewImages',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('url', sa.String(), nullable=False),
    # sa.Column('preview', sa.Boolean(), nullable=False),
    # sa.Column('reviewId', sa.Integer(), nullable=False),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=False),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=False),
    # sa.ForeignKeyConstraint(['reviewId'], ['reviews.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # if environment == "production":
    #     op.execute(f"ALTER TABLE reviewImages SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviewImages')
    op.drop_table('reviews')
    op.drop_table('productImages')
    op.drop_table('orderItems')
    op.drop_table('favorites')
    op.drop_table('cartItems')
    op.drop_table('shoppingCarts')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('users')
    # ### end Alembic commands ###
