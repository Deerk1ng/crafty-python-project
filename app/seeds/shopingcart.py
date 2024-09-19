from app.models import db, ShoppingCart, environment, SCHEMA
from sqlalchemy.sql import text


def seed_shopping_carts():
    #  Data for seeding cart items
    shopping_cart = [
        ShoppingCart(user_id=2, total=0),
        ShoppingCart(user_id=1, total=0),
        ShoppingCart(user_id=3, total=0),
        ShoppingCart(user_id=4, total=0),
    ]

    # Add all cart items to the session
    for items in shopping_cart:
        db.session.add(items)

    # Commit to db
    db.session.commit()



def undo_shopping_carts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shopping_carts"))

    db.session.commit()
