from app.models import db, OrderItem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_order_items():
    order1_item1 = OrderItem(
        order_id=1 ,product_id=3 , quantity=2)
    order1_item2 = OrderItem(
        order_id=1 ,product_id=10 , quantity=1)
    order1_item3 = OrderItem(
        order_id=1 ,product_id=12 , quantity=5)
    order1_item4 = OrderItem(
        order_id=1 ,product_id=6 , quantity=3)

    order2_item1 = OrderItem(
        order_id=2 ,product_id=1 , quantity=1)
    order2_item2 = OrderItem(
        order_id=2 ,product_id=2 , quantity=1)
    order2_item3 = OrderItem(
        order_id=2 ,product_id=5 , quantity=1)
    order2_item4 = OrderItem(
        order_id=2 ,product_id=8 , quantity=1)
    order2_item5 = OrderItem(
        order_id=2 ,product_id=13 , quantity=1)
    order2_item6 = OrderItem(
        order_id=2 ,product_id=15 , quantity=1)

    order3_item1 = OrderItem(
        order_id=3 ,product_id=4 , quantity=5)
    order3_item2 = OrderItem(
        order_id=3 ,product_id=9 , quantity=10)
    order3_item3 = OrderItem(
        order_id=3 ,product_id=11 , quantity=2)
    order3_item4 = OrderItem(
        order_id=3 ,product_id=7 , quantity=1)
    order3_item5 = OrderItem(
        order_id=3 ,product_id=14 , quantity=3)

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

def undo_order_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM order_items"))

    db.session.commit()
