from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviewImages():
    rev1_pic1 = ReviewImage(
        url='/review/image/1' ,preview=False , reviewId=1)
    rev6_pic1 = ReviewImage(
        url='/review/image/2' ,preview=False , reviewId=6)
    rev11_pic1 = ReviewImage(
        url='/review/image/3' ,preview=False , reviewId=11)
    rev16_pic1 = ReviewImage(
        url='/review/image/4' ,preview=False , reviewId=16)
    rev17_pic1 = ReviewImage(
        url='/review/image/5' ,preview=False , reviewId=17)
    rev21_pic1 = ReviewImage(
        url='/review/image/6' ,preview=False , reviewId=21)
    rev26_pic1 = ReviewImage(
        url='/review/image/7' ,preview=False , reviewId=26)
    rev31_pic1 = ReviewImage(
        url='/review/image/8' ,preview=False , reviewId=31)
    rev36_pic1 = ReviewImage(
        url='/review/image/9' ,preview=False , reviewId=36)
    rev37_pic1 = ReviewImage(
        url='/review/image/10' ,preview=False , reviewId=37)
    rev41_pic1 = ReviewImage(
        url='/review/image/11' ,preview=False , reviewId=41)
    rev46_pic1 = ReviewImage(
        url='/review/image/12' ,preview=False , reviewId=46)
    rev51_pic1 = ReviewImage(
        url='/review/image/13' ,preview=False , reviewId=51)
    rev56_pic1 = ReviewImage(
        url='/review/image/14' ,preview=False , reviewId=56)
    rev57_pic1 = ReviewImage(
        url='/review/image/15' ,preview=False , reviewId=57)

    db.session.add(rev1_pic1)
    db.session.add(rev6_pic1)
    db.session.add(rev11_pic1)
    db.session.add(rev16_pic1)
    db.session.add(rev17_pic1)
    db.session.add(rev21_pic1)
    db.session.add(rev26_pic1)
    db.session.add(rev31_pic1)
    db.session.add(rev36_pic1)
    db.session.add(rev37_pic1)
    db.session.add(rev41_pic1)
    db.session.add(rev46_pic1)
    db.session.add(rev51_pic1)
    db.session.add(rev56_pic1)
    db.session.add(rev57_pic1)
    db.session.commit()

def undo_reviewImages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviewImages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviewImages"))

    db.session.commit()
