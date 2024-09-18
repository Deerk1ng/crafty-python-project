from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():
    prod1_review1 = Review(
        user_id=2, product_id=1, item_rating=3, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod1_review2 = Review(
        user_id=3, product_id=1, item_rating=5, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod1_review3 = Review(
        user_id=4, product_id=1, item_rating=2, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod1_review4 = Review(
        user_id=6, product_id=1, item_rating=5, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod2_review1 = Review(
        user_id=2, product_id=2, item_rating=4, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod2_review2 = Review(
        user_id=3, product_id=2, item_rating=2, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod2_review3 = Review(
        user_id=4, product_id=2, item_rating=5, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod2_review4 = Review(
        user_id=6, product_id=2, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod3_review1 = Review(
        user_id=2, product_id=3, item_rating=1, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod3_review2 = Review(
        user_id=3, product_id=3, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod3_review3 = Review(
        user_id=4, product_id=3, item_rating=4, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod3_review4 = Review(
        user_id=6, product_id=3, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod4_review1 = Review(
        user_id=2, product_id=4, item_rating=2, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod4_review2 = Review(
        user_id=3, product_id=4, item_rating=1, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod4_review3 = Review(
        user_id=4, product_id=4, item_rating=1, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod4_review4 = Review(
        user_id=6, product_id=4, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod5_review1 = Review(
        user_id=2, product_id=5, item_rating=5, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod5_review2 = Review(
        user_id=3, product_id=5, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod5_review3 = Review(
        user_id=4, product_id=5, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod5_review4 = Review(
        user_id=6, product_id=5, item_rating=4, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod6_review1 = Review(
        user_id=2, product_id=6, item_rating=5, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod6_review2 = Review(
        user_id=3, product_id=6, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod6_review3 = Review(
        user_id=4, product_id=6, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod6_review4 = Review(
        user_id=6, product_id=6, item_rating=4, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod7_review1 = Review(
        user_id=2, product_id=7, item_rating=2, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod7_review2 = Review(
        user_id=3, product_id=7, item_rating=1, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod7_review3 = Review(
        user_id=4, product_id=7, item_rating=1, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod7_review4 = Review(
        user_id=6, product_id=7, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod8_review1 = Review(
        user_id=2, product_id=8, item_rating=5, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod8_review2 = Review(
        user_id=3, product_id=8, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod8_review3 = Review(
        user_id=4, product_id=8, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod8_review4 = Review(
        user_id=6, product_id=8, item_rating=4, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod9_review1 = Review(
        user_id=2, product_id=9, item_rating=5, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod9_review2 = Review(
        user_id=3, product_id=9, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod9_review3 = Review(
        user_id=4, product_id=9, item_rating=5, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod9_review4 = Review(
        user_id=5, product_id=9, item_rating=4, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod10_review1 = Review(
        user_id=2, product_id=10, item_rating=3, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod10_review2 = Review(
        user_id=3, product_id=10, item_rating=5, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod10_review3 = Review(
        user_id=4, product_id=10, item_rating=2, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod10_review4 = Review(
        user_id=5, product_id=10, item_rating=5, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod11_review1 = Review(
        user_id=2, product_id=11, item_rating=4, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod11_review2 = Review(
        user_id=3, product_id=11, item_rating=2, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod11_review3 = Review(
        user_id=4, product_id=11, item_rating=5, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod11_review4 = Review(
        user_id=5, product_id=11, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod12_review1 = Review(
        user_id=2, product_id=12, item_rating=1, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod12_review2 = Review(
        user_id=3, product_id=12, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod12_review3 = Review(
        user_id=4, product_id=12, item_rating=4, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod12_review4 = Review(
        user_id=5, product_id=12, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod13_review1 = Review(
        user_id=2, product_id=13, item_rating=3, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod13_review2 = Review(
        user_id=3, product_id=13, item_rating=4, shipping_rating=1, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod13_review3 = Review(
        user_id=4, product_id=13, item_rating=2, shipping_rating=1, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod13_review4 = Review(
        user_id=5, product_id=13, item_rating=5, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod14_review1 = Review(
        user_id=2, product_id=14, item_rating=5, shipping_rating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod14_review2 = Review(
        user_id=3, product_id=14, item_rating=3, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod14_review3 = Review(
        user_id=4, product_id=14, item_rating=5, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod14_review4 = Review(
        user_id=5, product_id=14, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod15_review1 = Review(
        user_id=2, product_id=15, item_rating=4, shipping_rating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod15_review2 = Review(
        user_id=3, product_id=15, item_rating=3, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod15_review3 = Review(
        user_id=4, product_id=15, item_rating=4, shipping_rating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod15_review4 = Review(
        user_id=5, product_id=15, item_rating=1, shipping_rating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    db.session.add(prod1_review1)
    db.session.add(prod1_review2)
    db.session.add(prod1_review3)
    db.session.add(prod1_review4)

    db.session.add(prod2_review1)
    db.session.add(prod2_review2)
    db.session.add(prod2_review3)
    db.session.add(prod2_review4)

    db.session.add(prod3_review1)
    db.session.add(prod3_review2)
    db.session.add(prod3_review3)
    db.session.add(prod3_review4)

    db.session.add(prod4_review1)
    db.session.add(prod4_review2)
    db.session.add(prod4_review3)
    db.session.add(prod4_review4)

    db.session.add(prod5_review1)
    db.session.add(prod5_review2)
    db.session.add(prod5_review3)
    db.session.add(prod5_review4)

    db.session.add(prod6_review1)
    db.session.add(prod6_review2)
    db.session.add(prod6_review3)
    db.session.add(prod6_review4)

    db.session.add(prod7_review1)
    db.session.add(prod7_review2)
    db.session.add(prod7_review3)
    db.session.add(prod7_review4)

    db.session.add(prod8_review1)
    db.session.add(prod8_review2)
    db.session.add(prod8_review3)
    db.session.add(prod8_review4)

    db.session.add(prod9_review1)
    db.session.add(prod9_review2)
    db.session.add(prod9_review3)
    db.session.add(prod9_review4)

    db.session.add(prod10_review1)
    db.session.add(prod10_review2)
    db.session.add(prod10_review3)
    db.session.add(prod10_review4)

    db.session.add(prod11_review1)
    db.session.add(prod11_review2)
    db.session.add(prod11_review3)
    db.session.add(prod11_review4)

    db.session.add(prod12_review1)
    db.session.add(prod12_review2)
    db.session.add(prod12_review3)
    db.session.add(prod12_review4)

    db.session.add(prod13_review1)
    db.session.add(prod13_review2)
    db.session.add(prod13_review3)
    db.session.add(prod13_review4)

    db.session.add(prod14_review1)
    db.session.add(prod14_review2)
    db.session.add(prod14_review3)
    db.session.add(prod14_review4)

    db.session.add(prod15_review1)
    db.session.add(prod15_review2)
    db.session.add(prod15_review3)
    db.session.add(prod15_review4)

    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
