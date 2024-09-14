from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text

def seed_products():
    chainmail = Product(
        ownerId='2' ,name='chainmail' , price='100.00' , description='This shirt made of interlocked metal rings is perfect for any medieval reinactment outfit you are looking for. Perfect for renfaires' , category='shirts' )

    db.session.add(chainmail)
    db.session.commit()

def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
