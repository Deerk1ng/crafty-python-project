from datetime import datetime
from .db import db, environment, SCHEMA

class Review(db.Model):
    __tablename__= 'reviews'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    productOwnerId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    itemRating = db.Column(db.Integer, nullable=False)
    shippingRating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    user = db.relationship('Users', back_populates='reviews')
    product = db.relationship('Product', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'productOwnerId': self.productOwnerId,
            'productId': self.productId,
            'itemRating': self.itemRating,
            'shippingRating': self.shippingRating,
            'description': self.description,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
