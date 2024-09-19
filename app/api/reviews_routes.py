from flask import Blueprint, jsonify, redirect, request
from app import db
from app.models import Product, Review, ReviewImage, User
from flask_login import current_user, login_required
from app.forms import CreateProductForm, CreateReviewForm

review_route = Blueprint('review', __name__)

@review_route.route('/')
def get_all_reviews():
    reviews = db.session.query(Review).all()

    reviewsList = []

    for review in reviews:
        reviewDict = review.to_dict()
        reviewsList.append(reviewDict)

    return jsonify({'reviews': reviewsList})

@review_route.route('/<int:review_id>', methods=['PUT'])
@login_required
def edit_review(review_id):
    """
    edits a review
    """
    logged_in_user = current_user.to_dict()

    if not logged_in_user:
        return redirect('/api/auth/unauthorized'), 401

    review_by_id = db.session.query(Review).filter(Review.id == review_id).first()

    if not review_by_id:
        return {'errors': {'message': 'Review does not exist'}}, 404

    if review_by_id.user_id == logged_in_user['id']:
        form = CreateReviewForm()

        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            review_by_id.item_rating = form.data['item_rating']
            review_by_id.shipping_rating = form.data['shipping_rating']
            review_by_id.description = form.data['description']

            db.session.commit()

            updated_review = review_by_id.to_dict()
            return {'updated_review': updated_review}, 201
        else:
            return form.errors, 400
    elif not review_by_id.user_id == logged_in_user['id']:
        return redirect('/api/auth/unauthorized'), 401

@review_route.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    logged_in_user = current_user.to_dict()

    if not logged_in_user:
        return redirect('/api/auth/unauthorized'), 401

    review_by_id = db.session.query(Review).filter(Review.id == review_id).first()

    if not review_by_id:
        return {'errors': {'message': 'Review does not exist'}}, 404

    if review_by_id.user_id == logged_in_user['id']:
        db.session.delete(review_by_id)
        db.session.commit()
        return {'message': 'Delete Successful'}, 200

    return {'error': 'Unauthorized to delete this review'}, 401
