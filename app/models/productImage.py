from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class ProductImage(db.Model):
    __tablename__= 'product_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    preview = db.Column(db.Boolean, default=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id'), ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    product = db.relationship('Product', back_populates='product_images')

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'preview': self.preview,
            'product_id': self.product_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
