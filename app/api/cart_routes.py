from flask import Blueprint, jsonify, session, redirect, request
from app import db
from app.models import ShoppingCart, CartItem, Product, ProductImage
from flask_login import current_user, login_required


cart_route = Blueprint('cart', __name__)


#Create shopping cart for user
@cart_route.route('/current', methods=['POST'])
@login_required
def createShoppingCart():
    currentUser = current_user.to_dict()
    user_id = currentUser['id']
    cart = ShoppingCart(
        user_id = user_id,
        total = 0
    )
    try:
        db.session.add(cart)
        db.session.commit()
        return {'shopping_cart': cart.to_dict()}
    except:
        return {'errors': {'message': 'There was an error creating shopping cart'}}


#Get items for Shopping Cart
@cart_route.route('/<int:cart_id>')
@login_required
def getShoppingCart(cart_id):
    cart_by_id = db.session.query(ShoppingCart).filter(ShoppingCart.id == cart_id).first()

    if not cart_by_id:
        return {'errors': {'message': 'Cart does not exist'}}, 404

    items = db.session.query(CartItem).filter(CartItem.cart_id == cart_id)
    items_dict = [item.to_dict() for item in items]

    # calculate cart total
    total = 0

    #get product info and images
    for item in items_dict:
        product = db.session.query(Product).filter(Product.id == item['product_id']).first()
        images = db.session.query(ProductImage).filter(ProductImage.product_id == item['product_id'])

        #add item cost to total
        item_price = product.price * item['quantity']
        total += item_price

        #add product and images to item
        item['product'] = product.to_dict()
        item['images'] = [image.to_dict() for image in images]



    cart_dict = cart_by_id.to_dict()
    cart_dict['items'] = items_dict
    cart_dict['total'] = total

    return {'shoppingCart': cart_dict}, 200

#Remove item to shopping cart
@cart_route.route('/<int:item_id>', methods=['DELETE'])
@login_required
def removeItem(item_id):

    cart_item = db.session.query(CartItem).filter(CartItem.id == item_id).first()

    try:
        db.session.delete(cart_item)
        db.session.commit()
        return {'message': 'Cart item successfuly deleted'}
    except:
        return {'errors': {'message': 'There was an error in deleted item from cart'}}


#While in PRODUCTS PAGE, add item to shopping cart
@cart_route.route('/<int:cart_id>/<int:product_id>', methods=['POST'])
@login_required
def addItem(cart_id, product_id):

    item = db.session.query(CartItem).filter(CartItem.cart_id == cart_id).filter(CartItem.product_id == product_id).first()

    #if item already in cart, add +1 to quantity
    if item:
        item.quantity = item.quantity + 1
        try:
            db.session.commit()
            return {'item': item.to_dict()}
        except:
            return {'errors': {'message': 'Could not update quantity of item'}}

    #if item not found in cart, add to cart
    if not item:
        new_item = CartItem(
            cart_id = cart_id,
            product_id = product_id,
            quantity = 1
        )
        try:
            db.session.add(new_item)
            db.session.commit()
            return {'new_item': new_item.to_dict()}
        except:
            return {'errors': {'message': 'Could not update add item to cart'}}


#While in CART, Add/Subtract quantity of item
