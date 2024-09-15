from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():
    prod1_review1 = Review(
        userId=2, productId=1, itemRating=3, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod1_review2 = Review(
        userId=3, productId=1, itemRating=5, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod1_review3 = Review(
        userId=4, productId=1, itemRating=2, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod1_review4 = Review(
        userId=5, productId=1, itemRating=5, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod2_review1 = Review(
        userId=2, productId=2, itemRating=4, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod2_review2 = Review(
        userId=3, productId=2, itemRating=2, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod2_review3 = Review(
        userId=4, productId=2, itemRating=5, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod2_review4 = Review(
        userId=5, productId=2, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod3_review1 = Review(
        userId=2, productId=3, itemRating=1, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod3_review2 = Review(
        userId=3, productId=3, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod3_review3 = Review(
        userId=4, productId=3, itemRating=4, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod3_review4 = Review(
        userId=5, productId=3, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod4_review1 = Review(
        userId=2, productId=4, itemRating=2, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod4_review2 = Review(
        userId=3, productId=4, itemRating=1, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod4_review3 = Review(
        userId=4, productId=4, itemRating=1, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod4_review4 = Review(
        userId=5, productId=4, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod5_review1 = Review(
        userId=2, productId=5, itemRating=5, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod5_review2 = Review(
        userId=3, productId=5, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod5_review3 = Review(
        userId=4, productId=5, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod5_review4 = Review(
        userId=5, productId=5, itemRating=4, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod6_review1 = Review(
        userId=2, productId=6, itemRating=5, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod6_review2 = Review(
        userId=3, productId=6, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod6_review3 = Review(
        userId=4, productId=6, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod6_review4 = Review(
        userId=5, productId=6, itemRating=4, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod7_review1 = Review(
        userId=2, productId=7, itemRating=2, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod7_review2 = Review(
        userId=3, productId=7, itemRating=1, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod7_review3 = Review(
        userId=4, productId=7, itemRating=1, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod7_review4 = Review(
        userId=5, productId=7, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod8_review1 = Review(
        userId=2, productId=8, itemRating=5, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod8_review2 = Review(
        userId=3, productId=8, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod8_review3 = Review(
        userId=4, productId=8, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod8_review4 = Review(
        userId=5, productId=8, itemRating=4, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod9_review1 = Review(
        userId=2, productId=9, itemRating=5, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod9_review2 = Review(
        userId=3, productId=9, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod9_review3 = Review(
        userId=4, productId=9, itemRating=5, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod9_review4 = Review(
        userId=5, productId=9, itemRating=4, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod10_review1 = Review(
        userId=2, productId=10, itemRating=3, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod10_review2 = Review(
        userId=3, productId=10, itemRating=5, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod10_review3 = Review(
        userId=4, productId=10, itemRating=2, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod10_review4 = Review(
        userId=5, productId=10, itemRating=5, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod11_review1 = Review(
        userId=2, productId=11, itemRating=4, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod11_review2 = Review(
        userId=3, productId=11, itemRating=2, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod11_review3 = Review(
        userId=4, productId=11, itemRating=5, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod11_review4 = Review(
        userId=5, productId=11, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod12_review1 = Review(
        userId=2, productId=12, itemRating=1, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod12_review2 = Review(
        userId=3, productId=12, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod12_review3 = Review(
        userId=4, productId=12, itemRating=4, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod12_review4 = Review(
        userId=5, productId=12, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod13_review1 = Review(
        userId=2, productId=13, itemRating=3, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod13_review2 = Review(
        userId=3, productId=13, itemRating=4, shippingRating=1, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod13_review3 = Review(
        userId=4, productId=13, itemRating=2, shippingRating=1, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod13_review4 = Review(
        userId=5, productId=13, itemRating=5, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod14_review1 = Review(
        userId=2, productId=14, itemRating=5, shippingRating=3, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod14_review2 = Review(
        userId=3, productId=14, itemRating=3, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod14_review3 = Review(
        userId=4, productId=14, itemRating=5, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod14_review4 = Review(
        userId=5, productId=14, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

    prod15_review1 = Review(
        userId=2, productId=15, itemRating=4, shippingRating=4, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod15_review2 = Review(
        userId=3, productId=15, itemRating=3, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod15_review3 = Review(
        userId=4, productId=15, itemRating=4, shippingRating=5, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')
    prod15_review4 = Review(
        userId=5, productId=15, itemRating=1, shippingRating=2, description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.')

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
