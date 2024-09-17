from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable= False)
    last_name = db.Column(db.String(40), nullable= False)
    shop_name = db.Column(db.String(40), nullable= False, unique=True)
    address = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), default=datetime.now(), nullable=False)

    products = db.relationship("Product", back_populates="owner")

    favorites = db.relationship("Favorite", back_populates="user")
    orders = db.relationship("Order", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")
    shoppingCart = db.relationship("ShoppingCart", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'shop_name' : self.shop_name,
            'address' : self.address
        }
