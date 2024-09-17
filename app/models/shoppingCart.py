from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class ShoppingCart(db.Model):
    __tablename__ = 'shoppingCarts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    total = db.Column(db.Float, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    user = db.relationship('User', back_populates='shoppingCart')
    cartItems = db.relationship('CartItem', back_populates='shoppingCart')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'total': self.total,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
