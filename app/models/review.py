from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__= 'reviews'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id"), ondelete="CASCADE"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id'), ondelete="CASCADE"), nullable=False)
    item_rating = db.Column(db.Integer, nullable=False)
    shipping_rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    user = db.relationship('User', back_populates='reviews')
    product = db.relationship('Product', back_populates='reviews')
    reviewImage = db.relationship('ReviewImage', back_populates='review', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'item_rating': self.item_rating,
            'shipping_rating': self.shipping_rating,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
