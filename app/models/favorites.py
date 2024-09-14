from datetime import datetime
from .db import db, environment, SCHEMA


class Favorite(db.Model):
    __tablename__ = 'favorites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    user = db.relationship('User', back_populates='favorites')
    product = db.relationship('Product', back_populates='favorites')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'productId': self.productId,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
