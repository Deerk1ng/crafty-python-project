from app.models import db, OrderItem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_orderItems():
    order1_item1 = OrderItem(
        orderId=1 ,productId=3 , quantity=2)
    order1_item2 = OrderItem(
        orderId=1 ,productId=10 , quantity=1)
    order1_item3 = OrderItem(
        orderId=1 ,productId=12 , quantity=5)
    order1_item4 = OrderItem(
        orderId=1 ,productId=6 , quantity=3)

    order2_item1 = OrderItem(
        orderId=2 ,productId=1 , quantity=1)
    order2_item2 = OrderItem(
        orderId=2 ,productId=2 , quantity=1)
    order2_item3 = OrderItem(
        orderId=2 ,productId=5 , quantity=1)
    order2_item4 = OrderItem(
        orderId=2 ,productId=8 , quantity=1)
    order2_item5 = OrderItem(
        orderId=2 ,productId=13 , quantity=1)
    order2_item6 = OrderItem(
        orderId=2 ,productId=15 , quantity=1)

    order3_item1 = OrderItem(
        orderId=3 ,productId=4 , quantity=5)
    order3_item2 = OrderItem(
        orderId=3 ,productId=9 , quantity=10)
    order3_item3 = OrderItem(
        orderId=3 ,productId=11 , quantity=2)
    order3_item4 = OrderItem(
        orderId=3 ,productId=7 , quantity=1)
    order3_item5 = OrderItem(
        orderId=3 ,productId=14 , quantity=3)

    db.session.add(order1_item1)
    db.session.add(order1_item2)
    db.session.add(order1_item3)
    db.session.add(order1_item4)

    db.session.add(order2_item1)
    db.session.add(order2_item2)
    db.session.add(order2_item3)
    db.session.add(order2_item4)
    db.session.add(order2_item5)
    db.session.add(order2_item6)

    db.session.add(order3_item1)
    db.session.add(order3_item2)
    db.session.add(order3_item3)
    db.session.add(order3_item4)
    db.session.add(order3_item5)

    db.session.commit()

def undo_orderItems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.orderItems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orderItems"))

    db.session.commit()
