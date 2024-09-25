from flask import Blueprint, jsonify, redirect, request
from app import db
from app.models import Product, Review, ProductImage, ReviewImage, User, Favorite
from flask_login import current_user, login_required
# create "create product form" and import it
from app.forms import CreateProductForm, CreateReviewForm, CreateImageForm



product_route = Blueprint('products', __name__)

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
        user = db.session.query(User).filter(User.id == productById.owner_id).first().to_dict()

        user_info = {'id': user['id'], 'shop_name': user['shop_name']}


        # Add images to the productById dictionary
        if len(reviews):
            reviewLngth = len(reviews)
        else:
            reviewLngth = 1
        itemRte = 0
        shippingRte = 0

        # grab the ratings from the reviews and divide them by len of reviews
        for review in reviews:
            itemRte += review.item_rating
            shippingRte += review.shipping_rating

        # avgRating added to data
        productDict['owner'] = user_info
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
        user = db.session.query(User).filter(User.id == productDict['owner_id']).first().to_dict()

        # just grabbng id and shop_name
        user_info = {'id': user['id'], 'shop_name': user['shop_name']}

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
        productDict['owner'] = user_info
        productDict['avgRating'] = avg_rating
        productDict['images'] = [image.to_dict() for image in images]
        productDict['reviews'] = [review.to_dict() for review in reviews]

        # Append the productById dictionary to the list
        productsList.append(productDict)
    # Return the JSON response
    return jsonify(productsList)


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
    user = db.session.query(User).filter(User.id == product_dict['owner_id']).first().to_dict()

    # just grabbng id and shop_name
    user_info = {'id': user['id'], 'first_name': user['first_name']}

    # review avg rating
    review_length = len(reviews)
    item_rating_sum = 0
    shipping_rating_sum = 0

    reviews_list = []

    for review in reviews:
        item_rating_sum += review.item_rating
        shipping_rating_sum += review.shipping_rating
        r = review.to_dict()
        review_images = db.session.query(ReviewImage).filter(ReviewImage.review_id == review.id).all()
        r['images'] = [review_image.to_dict() for review_image in review_images]
        reviews_list.append(r)



    avg_rating = 0
    if review_length > 0:
        avg_rating = (item_rating_sum + shipping_rating_sum) / (2 * review_length)

    product_dict['owner'] = user_info
    product_dict['images'] = [image.to_dict() for image in images]
    product_dict['reviews'] = reviews_list #[review.to_dict() for review in reviews]
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
            owner_id= currentUser['id'],
            name= form.data['name'],
            price= form.data['price'],
            description= form.data['description'],
            category= form.data['category'],
        )

        db.session.add(product)
        db.session.commit()
        new_product = product.to_dict()

        return {'created_product' :new_product}, 201

    return form.errors, 400


@product_route.route('/<int:product_id>', methods=['PUT'])
@login_required
def editProduct(product_id):
    """
    Edits a product and returns the updated product's details in JSON format
    """
    logged_in_user = current_user.to_dict()

    product_by_id = db.session.query(Product).filter(Product.id == product_id).first()

    if not product_by_id:
        return {'errors': {'message': 'Product does not exist'}}, 404

    if product_by_id.owner_id != logged_in_user['id']:
        return {'errors': {'message': 'Unauthorized to edit this product'}}, 403

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

        return {'updated_product': updated_product}, 200

    return form.errors, 400

@product_route.route('/<int:product_id>/images', methods=['POST'])
@login_required
def add_image_to_product(product_id):
    logged_in_user = current_user.to_dict()

    if not logged_in_user:
        return redirect('/api/auth/unauthorized'), 401

    product_by_id = db.session.query(Product).filter(Product.id == product_id).first()

    if not product_by_id:
        return {'errors': {'message': 'Product does not exist'}}, 404

    if product_by_id.owner_id == logged_in_user['id']:
        form = CreateImageForm()

        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            image = ProductImage(
                url = form.data['url'],
                preview = form.data['preview'],
                product_id = product_id
            )

            db.session.add(image)
            db.session.commit()
            new_image = image.to_dict()

            return {'new_image': new_image}, 201
        else:
            return form.errors, 400
    elif not product_by_id.owner_id == logged_in_user['id']:
        return redirect('/api/auth/unauthorized'), 401

########
@product_route.route('/<int:product_id>/images/<int:image_id>', methods=['DELETE'])
@login_required
def delete_product_image(product_id, image_id):
    logged_in_user = current_user.to_dict()

    if not logged_in_user:
        return redirect('/api/auth/unauthorized'), 401

    image_by_id = db.session.query(ProductImage).filter(ProductImage.id == image_id).first()

    if not image_by_id:
        return {'errors': {'message': 'Product Image does not exist'}}, 404

    product_by_id = db.session.query(Product).filter(Product.id == product_id).first()

    if product_by_id.owner_id == logged_in_user['id']:
        db.session.delete(image_by_id)
        db.session.commit()
        return {'Message': 'Delete Successful'}, 200

    return {'error': 'Unauthorized to delete this Product Image'}, 401


@product_route.route('/<int:product_id>', methods=['DELETE'])
@login_required
def deleteProduct(product_id):
    """
    Deletes a product and redirect user to their listings
    """
    currentUser = current_user.to_dict()

    productById = db.session.query(Product).filter(Product.id == product_id).first()

    if not productById:
        return {'error': 'Product does not exist'}, 404

    if productById.owner_id == currentUser['id']:
        db.session.delete(productById)
        db.session.commit()
        return {'message': "product deleted successfuly"}, 200

    return {'error': 'Unauthorized to delete this productById'}, 401

@product_route.route('/<int:product_id>/reviews')
def get_reviews_by_product_id(product_id):
    productById = db.session.query(Product).filter(Product.id == product_id).first()

    if not productById:
        return {'error': 'Product does not exist'}, 404

    reviews = db.session.query(Review).filter(Review.product_id == product_id).all()
    reviewsList = []

    for review in reviews:
        reviewDict = review.to_dict()

        images = db.session.query(ReviewImage).filter(ReviewImage.review_id == review.id)
        user = db.session.query(User).filter(User.id == reviewDict['user_id']).first().to_dict()

        # just grabbng id and shop_name
        user_info = {'id': user['id'], 'name': user['first_name']}
        reviewDict['user'] = user_info
        reviewDict['image'] = [image.to_dict() for image in images]
        reviewsList.append(reviewDict)
    return jsonify({'reviews': reviewsList})

@product_route.route('/<int:product_id>/reviews', methods=['POST'])
@login_required
def create_review_by_product_id(product_id):
    currentUser = current_user.to_dict()
    productById = db.session.query(Product).filter(Product.id == product_id).first()

    if not productById:
        return {'error': 'Product does not exist'}, 404


    product_reviews = db.session.query(Review).join(Product).filter(Product.id == product_id).filter(Review.user_id == currentUser['id']).one_or_none()

    if product_reviews:
        return {'error': 'User already has a review for this product'}, 403



    form = CreateReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review(
            user_id = currentUser['id'],
            product_id = product_id,
            item_rating = form.data['item_rating'],
            shipping_rating = form.data['shipping_rating'],
            description = form.data['description']
        )

        db.session.add(review)
        db.session.commit()
        new_review = review.to_dict()

        return {'created_review': new_review}

    return form.errors, 400



# Add to favorites route
@product_route.route('/<int:productId>/favorites', methods=["POST"])
@login_required
def add_to_favorites(productId):
    """
    add current productId to current users favorites
    """
    check_fav = db.session.query(Favorite).filter(Favorite.product_id == productId, Favorite.user_id == current_user.id).first()

    check_product = db.session.query(Product).filter(Product.id == productId).first()

    if not check_product:
        return {'error': "Product does not exist"}, 404

    if not check_fav:
        new_fav = Favorite(
            user_id = current_user.id,
            product_id = productId
        )

        db.session.add(new_fav)
        db.session.commit()

        new_fav.to_dict()
        return {"message": 'Product added to favorites successfully!', "fav": new_fav.to_dict()}, 201
    else:
        return {'error': 'Product is already added to favorites'}
