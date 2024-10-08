from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', first_name='Demo', last_name='Lition', shop_name="Demo's Products", address="California")
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password',first_name='Marnie', last_name='Marie', shop_name="Marnie's Clothes", address="New York")
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password',first_name='Bobbie', last_name='Borden', shop_name="Props by Bob", address="Colorado")
    johnny = User(
        username='johnny', email="johnny@aa.io", password='password', first_name='Johnny', last_name='Johnson', shop_name="John's jeans", address="Conneticut")
    jane = User(
        username='jane', email="jane@aa.io", password='password',first_name='Jane', last_name='Bert', shop_name="Jane's Cardboard Weapons", address="Illinois")
    sarah = User(
        username='sarah', email="sarah@aa.io", password='password',first_name='Sarah', last_name='Hertz', shop_name="Sarah's Bows and Strings", address="Texas")

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(johnny)
    db.session.add(jane)
    db.session.add(sarah)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
