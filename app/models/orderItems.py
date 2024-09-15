from datetime import datetime
from .db import db, environment, SCHEMA


class OrderItem(db.Model):
    __tablename__ = 'orderItems'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    order = db.relationship('Order', back_populates='orderItems')
    product = db.relationship('Product', back_populates='cartItems') ## shouldn't this also be orderItems?

    def to_dict(self):
        return {
            'id': self.id,
            'orderId': self.orderId,
            'productId': self.productId,
            'quantity': self.quantity,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
