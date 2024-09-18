from flask import Blueprint, jsonify, session, redirect, request
from app import db
from app.models import Product, Review, ProductImage, User
from flask_login import current_user, login_required
# create "create product form" and import it
from app.forms import CreateProductForm



product_route = Blueprint('productById', __name__)

@product_route.route('/')
def homeAllProducts():
    """
    Gets all products
    """
    products = db.session.query(Product).all()

    # create empty list
    productsList = []

    for productById in products:
        # Convert productById to dictionary
        productDict = productById.to_dict()

        # Query for images related to the current productById
        images = db.session.query(ProductImage).filter(ProductImage.product_id == productById.id).all()
        reviews = db.session.query(Review).filter(Review.product_id == productById.id).all()
        # Add images to the productById dictionary
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

        # Append the productById dictionary to the list
        productsList.append(productDict)

    # Return the JSON response
    return jsonify(productsList)


@product_route.route('/current')
@login_required
def productsForUser():
    """
    Gets all products for the current user logged in
    """
    # Convert current_user to a dictionary
    currentUser = current_user.to_dict()

    # Query products where the owner_id matches the current user's ID
    products = db.session.query(Product).filter(Product.owner_id == currentUser['id']).all()

    productsList = []

    for productById in products:
        # Convert productById to dictionary
        productDict = productById.to_dict()

        # Query for images and reviews related to the current productById
        images = db.session.query(ProductImage).filter(ProductImage.product_id == productById.id).all()
        reviews = db.session.query(Review).filter(Review.product_id == productById.id).all()

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

        # Add images, reviews, and average rating to the productById dictionary
        productDict['avgRating'] = avg_rating
        productDict['images'] = [image.to_dict() for image in images]
        productDict['reviews'] = [review.to_dict() for review in reviews]

        # Append the productById dictionary to the list
        productsList.append(productDict)
    # Return the JSON response
    return jsonify({'currentUser': currentUser}, {'products': productsList})


@product_route.route('/<int:product_id>')
def productById(product_id):
    """
    Gets product by product_id
    """
    productById = db.session.query(Product).filter(Product.id == product_id).first()

    if not productById:
        return {'error': 'Product does not exist'}, 404


    product_dict = productById.to_dict()

    images = db.session.query(ProductImage).filter(ProductImage.product_id == product_id).all()
    reviews = db.session.query(Review).filter(Review.product_id == product_id).all()

    # review avg rating
    review_length = len(reviews)
    item_rating_sum = 0
    shipping_rating_sum = 0

    for review in reviews:
        item_rating_sum += review.item_rating
        shipping_rating_sum += review.shipping_rating


    avg_rating = 0
    if review_length > 0:
        avg_rating = (item_rating_sum + shipping_rating_sum) / (2 * review_length)


    product_dict['images'] = [image.to_dict() for image in images]
    product_dict['reviews'] = [review.to_dict() for review in reviews]
    product_dict['avgRating'] = avg_rating



    return {'product': product_dict}


@product_route.route('/', methods=['POST'])
@login_required
def createProduct():
    """
    Creates a new product and redirects to new product
    """
    currentUser = current_user.to_dict()

    form = CreateProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        product = Product(
            owner_id= currentUser.id,
            name= form.data['name'],
            price= form.data['price'],
            description= form.data['description'],
            category= form.data['category'],
        )

        db.session.add(product)
        db.session.commit()
        new_product = product.to_dict()

        return {'created_product' :new_product}, redirect(f'/api/products/{new_product.id}'), 201

    return form.errors, 400


@product_route.route('/<int:product_id>', methods=['PUT'])
@login_required
def editProduct(product_id):
    """
    edits a product and redirects user to the product after submitting data
    """
    logged_in_user = current_user.to_dict()

    product_by_id = db.session.query(Product).filter(Product.id == product_id).first()

    if not logged_in_user:
        return redirect('/api/auth/unauthorized'), 401

    if not product_by_id:
        return {'errors': {'message': 'Product does not exist'}}, 404

    if product_by_id.owner_id == logged_in_user.id:
        form = CreateProductForm()

        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            if form.data.get('name'):
                product_by_id.name = form.data['name']
            if form.data.get('price'):
                product_by_id.price = form.data['price']
            if form.data.get('description'):
                product_by_id.description = form.data['description']
            if form.data.get('category'):
                product_by_id.category = form.data['category']

            db.session.commit()

            updated_product = product_by_id.to_dict()

            return {'updated_product': updated_product}, redirect(f'/api/products/{updated_product.id}'), 201
        elif not product_by_id.owner_id == logged_in_user.id:
            return redirect('/api/auth/unauthorized'), 401
        else:
            return form.errors, 400








@product_route.route('/<int:product_id>', methods=['DELETE'])
@login_required
def deleteProduct(product_id):
    """
    Deletes a product and redirect user to their listings
    """
    currentUser = current_user.to_dict()

    productById = db.session.query(Product).filter(Product.id == product_id).first()

    if not productById:
        return {'error': 'Product does not exist'}, 403

    if productById.owner_id == currentUser['id']:
        db.session.delete(productById)
        db.session.commit()
        return redirect('/api/products/current')

    return {'error': 'Unauthorized to delete this productById'}, 401
