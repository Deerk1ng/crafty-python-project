from datetime import datetime
from .db import db, environment, SCHEMA


class ShoppingCart(db.Model):
    __tablename__ = 'shoppingCart'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total = db.Column(db.Decimal, nullable=False)
    createdAt = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)

    user = db.relationship('User', back_populates='shoppingCart')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'total': self.total,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
