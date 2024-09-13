from datetime import datetime
from .db import db, environment, SCHEMA


class ReviewImage(db.Model):
    __tablename__ = 'reviewImages'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    preview = db.Column(db.Boolean, default=False, nullable=False)
    reviewId = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)
    createdAt = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)

    review = db.relationship('Review', back_populates='reviewImages')

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'preview': self.preview,
            'reviewId': self.reviewId,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
