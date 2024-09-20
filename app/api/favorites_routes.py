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

    favorites = db.session.query(Favorite).filter(currentUser['id'] == Favorite.user_id).all()
    favorites_list = []

    for favorite in favorites:
        favorite_dict = favorite.to_dict()


        product = db.session.query(Product).filter(Product.id == favorite_dict['product_id']).first()

        if not product:
            continue  # Skip if product not found

        product_dict = product.to_dict()

        # Grab images for the product
        images = db.session.query(ProductImage).filter(ProductImage.product_id == product_dict['id']).all()
        product_dict['images'] = [image.to_dict() for image in images]

        # Get product owner info
        product_user = db.session.query(User).filter(User.id == product_dict['owner_id']).first()
        product_dict['owner'] = product_user.to_dict() if product_user else None

        # Calculate avgRating based on reviews
        reviews = db.session.query(Review).filter(Review.product_id == product_dict['id']).all()
        item_rating_sum = 0
        shipping_rating_sum = 0
        review_length = len(reviews)

        if review_length > 0:
            for review in reviews:
                item_rating_sum += review.item_rating
                shipping_rating_sum += review.shipping_rating

            avg_rating = (item_rating_sum + shipping_rating_sum) / (2 * review_length)
        else:
            avg_rating = None

        product_dict['avgRating'] = avg_rating
        favorites_list.append(product_dict)

    return {'products': favorites_list}


@favorite_route.route('/<int:favoriteId>', methods=['DELETE'])
@login_required
def deleteFav(favoriteId):
    favorite = db.session.query(Favorite).filter(Favorite.id == favoriteId).first()


    if not favorite:
        return {'error': 'favorite does not exist'}, 404

    favorite_dict = favorite.to_dict()

    if favorite_dict["user_id"] == current_user.id:
        db.session.delete(favorite)
        db.session.commit()
        return {'message': "product deleted successfuly from favorites"}, 200


    return {'error': 'favorite does not exist'}, 404
