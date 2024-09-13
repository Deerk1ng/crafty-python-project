from datetime import datetime
from .db import db, environment, SCHEMA


class ProductImages(db.Model):
    __tablename__= 'productImages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    preview = db.Column(db.Boolean, default=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.id', nullable=False))
    createdAt = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)

    product = db.relationship('Product', back_populates='productImages')

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'preview': self.preview,
            'productId': self.productId,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
