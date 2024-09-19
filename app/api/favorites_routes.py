from flask import Blueprint, jsonify, redirect, request
from app import db
from app.models import Product, Review, ProductImage, ReviewImage, User, Favorite
from flask_login import current_user, login_required
# create "create product form" and import it
from app.forms import CreateProductForm, CreateReviewForm


favorite_route = Blueprint('favorites', __name__)

@favorite_route.route('/current')
@login_required
def favoritesByUserId():
    currentUser = current_user.to_dict()

    if not currentUser:
        return {'error': 'Must log in first'}, 404

    favorites = db.session.query(Favorite).filter(currentUser['id'] == Favorite.user_id).all()

    favorites_list = []

    # counter for ratings

    for favorite in favorites:
        favorite_dict = favorite.to_dict()

        products = db.session.query(Product).filter(Product.id == favorite_dict['product_id']).first().to_dict()

        # grab images just in case and add to product dict
        images = db.session.query(ProductImage).filter(products['id'] == ProductImage.id).all()
        products['images'] = [image.to_dict() for image in images]


        # find the user and add to the products dict
        product_user = db.session.query(User).filter(products['owner_id'] == User.id).first().to_dict()
        products['owner'] = product_user

        # reviews for avgRating
        reviews = db.session.query(Review).filter(products['id'] == Review.product_id).all()

        item_rating_sum = 0
        shipping_rating_sum = 0
        review_length = len(reviews)

        for review in reviews:
            item_rating_sum += review.item_rating
            shipping_rating_sum += review.shipping_rating

        if review_length > 0:
            avg_rating = (item_rating_sum + shipping_rating_sum) / (2 * review_length)

        products['avgRating'] = avg_rating

        favorites_list.append(products)

    return {products: favorites_list}
