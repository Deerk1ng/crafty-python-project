from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    name = db.Column(db.String(40))
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    owner = db.relationship("User", back_populates="products")
    favorites = db.relationship("Favorite", back_populates="product")
    cart_items = db.relationship("CartItem", back_populates="product")
    order_items = db.relationship("OrderItem", back_populates="product")
    product_images = db.relationship("ProductImage", back_populates="product")
    reviews = db.relationship("Review", back_populates="product")

    def to_dict(self):
        return {
            'id' : self.id,
            'owner_id' : self.owner_id,
            'name': self.name,
            'price' : self.price,
            'description' : self.description,
            'category' : self.category
        }
