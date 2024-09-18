from flask import Blueprint, jsonify, session, redirect
from app import db
from app.models import Product, Review, ProductImage, User
from flask_login import current_user, login_required



product_route = Blueprint('product', __name__)

@product_route.route('/')
def homeAllProducts():
    products = db.session.query(Product).all()

    # create empty list
    productsList = []

    for product in products:
        # Convert product to dictionary
        productDict = product.to_dict()

        # Query for images related to the current product
        images = db.session.query(ProductImage).filter(ProductImage.product_id == product.id).all()
        reviews = db.session.query(Review).filter(Review.product_id == product.id).all()
        # Add images to the product dictionary
        reviewLngth = len(reviews)
        itemRte = 0
        shippingRte = 0

        # grab the ratings from the reviews and divide them by len of reviews
        for review in reviews:
            itemRte += review.item_rating
            shippingRte += review.shipping_rating

        # avgRating added to data
        productDict['avgRating'] = (itemRte + shippingRte) / reviewLngth
        productDict['images'] = [image.to_dict() for image in images]
        productDict['reviews'] = [review.to_dict() for review in reviews]

        # Append the product dictionary to the list
        productsList.append(productDict)

    # Return the JSON response
    return jsonify(productsList)


@product_route.route('/current')
@login_required
def productsForUser():
    # Convert current_user to a dictionary
    currentUser = current_user.to_dict()

    # Query products where the owner_id matches the current user's ID
    products = db.session.query(Product).filter(Product.owner_id == currentUser['id']).all()

    productsList = []

    for product in products:
        # Convert product to dictionary
        productDict = product.to_dict()

        # Query for images and reviews related to the current product
        images = db.session.query(ProductImage).filter(ProductImage.product_id == product.id).all()
        reviews = db.session.query(Review).filter(Review.product_id == product.id).all()

        # Calculate average ratings
        review_length = len(reviews)
        item_rating_sum = 0
        shipping_rating_sum = 0

        for review in reviews:
            item_rating_sum += review.item_rating
            shipping_rating_sum += review.shipping_rating

        # Avoid division by zero
        avg_rating = 0
        if review_length > 0:
            avg_rating = (item_rating_sum + shipping_rating_sum) / (2 * review_length)

        # Add images, reviews, and average rating to the product dictionary
        productDict['avgRating'] = avg_rating
        productDict['images'] = [image.to_dict() for image in images]
        productDict['reviews'] = [review.to_dict() for review in reviews]

        # Append the product dictionary to the list
        productsList.append(productDict)
    # Return the JSON response
    return jsonify({'currentUser': currentUser}, {'products': productsList})





@product_route.route('/:product_id')
@login_required
def deleteProduct(product_id):
    currentUser = current_user.to_dict()

    product = db.session.query(Product).filter(Product.id == product_id)

    if not product:
        return {'error': 'Product does not exist'}, 404

    if product and product.owner_id == currentUser.id:
        db.session.delete(product)
        db.session.commit()
        return redirect('api/products/current')
