from datetime import datetime
from .db import db, environment, SCHEMA


class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(40))
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    owner = db.relationship("User", back_populates="products")

    def to_dict(self):
        return {
            'id' : self.id,
            'ownerId' : self.ownerId,
            'name': self.name,
            'price' : self.price,
            'description' : self.description,
            'category' : self.category
        }
