from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("shopping_carts.id")), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    cart = db.relationship('shopping_cart', back_populates='cart_items')
    product = db.relationship("Product", back_populates="cart_items")
    shopping_cart = db.relationship("shopping_cart", back_populates="cart_items")

    def to_dict(self):
        return {
            'id': self.id,
            'cart_id': self.cart_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
