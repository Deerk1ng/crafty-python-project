from flask import Blueprint, jsonify, session
from app import db
from app.models import Product, Review, ProductImage


product_route = Blueprint('product', __name__)

@product_route.route('/')
def homeAllProducts():
    # Query for all products including images and reviews
    # products = db.session.query(Product)
    # # images = db.session.query(ProductImage)


    # # Convert each product to a dictionary (assuming you have a to_dict method in your model)

    # # products_list = [product.to_dict() for product in products]
    # products_list = []

    # for product in products:
    #     # products_list.append(product.to_dict())
    #     images = db.session.query(ProductImage).filter( product.id == ProductImage.productId)
    #     # newProd = product.to_dict()
    #     # newProd['images'] = images.to_dict()
    #     # products_list.append(newProd)
    #     products_list.append(images.to_dict())

    # # productsImages_list = [productImg.to_dict() for productImg in images]


    # # Return the JSON response
    # return jsonify(products_list)
        products = db.session.query(Product).options(db.joinedload(Product.images)).all()

    # Convert each product to a dictionary and include images
        products_list = []
        for product in products:
            product_dict = product.to_dict()  # Convert product to dict

            # Add the images to the product dictionary
            product_dict['images'] = [image.to_dict() for image in product.images]
    
            # Append the product dictionary to the list
            products_list.append(product_dict)

        # Return the JSON response
        return jsonify(products_list)
