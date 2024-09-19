from app.models import db, CartItem, environment, SCHEMA
from sqlalchemy.sql import text


def seed_cart_items():
    #  Data for seeding cart items
    cart_items = [
        CartItem(cart_id=1, product_id=5, quantity=2),
        CartItem(cart_id=1, product_id=7, quantity=1),
        CartItem(cart_id=1, product_id=9, quantity=1),
        CartItem(cart_id=2, product_id=4, quantity=1),
        CartItem(cart_id=2, product_id=3, quantity=4),
        CartItem(cart_id=3, product_id=8, quantity=2),
        CartItem(cart_id=4, product_id=1, quantity=3),
    ]

    # Add all cart items to the session
    for item in cart_items:
        db.session.add(item)

    # Commit to db
    db.session.commit()



def undo_cart_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cart_items"))

    db.session.commit()
