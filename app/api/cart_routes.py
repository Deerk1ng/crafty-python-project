from flask import Blueprint, jsonify, session, redirect
from app import db
from app.models import ShoppingCart, CartItem, Product, ProductImage
from flask_login import current_user, login_required


cart_route = Blueprint('cart', __name__)


#Create/delete shopping cart for user
@cart_route.route('/current', methods=['POST', 'DELETE'])
@login_required
def createShoppingCart():
    currentUser = current_user.to_dict()
    cart = ShoppingCart(
        user_id= currentUser['id'],
        total= 0
    )
    try:
        db.session.add(cart)
        db.session.commit()
        return redirect('/current')
    except:
        return {'errors': {'message': 'There was an error creating cart'}}


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

#Add item to shopping cart
@cart_route.route('/<int:cart_id>/<int:item_id>', methods=['POST', 'DELETE'])
@login_required
def addItem(cart_id, item_id):
    return {cart_id, item_id}, 200
