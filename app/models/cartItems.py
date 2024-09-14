from datetime import datetime
from .db import db, environment, SCHEMA


class CartItem(db.Model):
    __tablename__ = 'cartItems'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    cartId = db.Column(db.Integer, db.ForeignKey("shoppingCarts.id"), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    cart = db.relationship('ShoppingCart', back_populates='cartItems')
    product = db.relationship('Product', back_populates='cartItems')

    def to_dict(self):
        return {
            'id': self.id,
            'cartId': self.cartId,
            'productId': self.productId,
            'quantity': self.quantity,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
