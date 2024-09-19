from app.models import db, Favorite, environment, SCHEMA
from sqlalchemy.sql import text


def seed_favorites():
    #  Data for seeding cart items
    favorites = [
        Favorite(user_id=2, product_id=14),
        Favorite(user_id=1, product_id=2),
        Favorite(user_id=1, product_id=12),
        Favorite(user_id=2, product_id=3),
        Favorite(user_id=3, product_id=1),
        Favorite(user_id=3, product_id=7),
        Favorite(user_id=4, product_id=11),
        Favorite(user_id=4, product_id=14),
        Favorite(user_id=4, product_id=5),
        Favorite(user_id=5, product_id=12),
        Favorite(user_id=1, product_id=6),
        Favorite(user_id=1, product_id=8),
    ]

    # Add all cart items to the session
    for item in favorites:
        db.session.add(item)

    # Commit to db
    db.session.commit()



def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))

    db.session.commit()
