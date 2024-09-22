from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class ReviewImage(db.Model):
    __tablename__ = 'review_images'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    preview = db.Column(db.Boolean, default=False, nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('reviews.id'), ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    review = db.relationship('Review', back_populates='reviewImage')

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'preview': self.preview,
            'review_id': self.review_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
