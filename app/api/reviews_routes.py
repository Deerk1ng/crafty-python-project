from flask import Blueprint, jsonify, session, redirect
from app import db
from app.models import Product, Review, ReviewImage, User
from flask_login import current_user, login_required

review_route = Blueprint('review', __name__)

@review_route.route('/')
def get_all_reviews():
    reviews = db.session.query(Review).all()

    reviewsList = []

    for review in reviews:
        reviewDict = review.to_dict()
        reviewsList.append(reviewDict)

    return jsonify({'reviews': reviewsList})

@review_route.route('/<product_id>')
def get_reviews_by_product_id(product_id):
    reviews = db.session.query(Review).filter(Review.product_id == product_id).all()
    reviewsList = []

    for review in reviews:
        reviewDict = review.to_dict()

        images = db.session.query(ReviewImage).filter(ReviewImage.review_id == review.id)

        reviewDict['image'] = [image.to_dict() for image in images]
        reviewsList.append(reviewDict)
    return jsonify({'reviews': reviewsList})
