from flask import Blueprint, request
from app import db
from app.models import ShoppingCart, CartItem, Product, Order, OrderItem, ProductImage, User
from flask_login import current_user, login_required


cart_route = Blueprint('cart', __name__)


#Get current user shopping cart and items, or create shopping cart for user
@cart_route.route('/current', methods=['GET', 'POST'])
@login_required
def getShoppingCart():

    user_id = current_user.id
    cart = db.session.query(ShoppingCart).filter(ShoppingCart.user_id == user_id).first()

    if(cart):
        cart_id = cart.id
        items = db.session.query(CartItem).filter(CartItem.cart_id == cart_id)
        items_dict = [item.to_dict() for item in items]

    # calculate cart total
        total = 0

    #get product info and images
        for item in items_dict:
            product = db.session.query(Product).filter(Product.id == item['product_id']).first()
            images = db.session.query(ProductImage).filter(ProductImage.product_id == item['product_id'])
            owner = db.session.query(User).filter(User.id == product.owner_id).first()

            #add item cost to total
            item_price = product.price * item['quantity']
            total += item_price

            #add product and images to item
            item['product'] = product.to_dict()
            item['images'] = [image.to_dict() for image in images] #should maybe just get the first image
            item['owner'] = owner.to_dict()

        #set total of cart
        cart.total = total
        db.session.commit()

        cart_dict = cart.to_dict()
        cart_dict['items'] = items_dict
        cart_dict['total'] = total

        return {'shopping_cart': cart_dict}, 200

    else: #makes new cart if no cart found
        cart = ShoppingCart(
            user_id = user_id,
            total = 0
        )
        db.session.add(cart)
        db.session.commit()
        return {'shopping_cart': cart.to_dict()}, 201



@cart_route.route('/current/<int:cart_id>', methods=['DELETE'])
@login_required
def deleteShoppingCart(cart_id): #can't delete a shopping cart if it has items in it
    cart = db.session.query(ShoppingCart).filter(ShoppingCart.id == cart_id).first()
    user_id = current_user.id
    if (user_id == cart.user_id):
        db.session.delete(cart)
        db.session.commit()
        return {'message': 'Shopping cart successfuly deleted'}, 200
    else:
        return {'errors': {'message': 'There was an error deleting shopping cart'}}

#Get items for Shopping Cart with cart id, sets total of cart
@cart_route.route('/<int:cart_id>')
@login_required
def getItems(cart_id):
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
        item['images'] = [image.to_dict() for image in images] #should maybe just get the first image


    #set total of cart
    cart_by_id.total = total
    db.session.commit()

    cart_dict = cart_by_id.to_dict()
    cart_dict['items'] = items_dict
    cart_dict['total'] = total

    return {'shoppingCart': cart_dict}, 200

#Add quantity to item via ITEM id
@cart_route.route('/add/<int:item_id>/<int:quantity>', methods=['POST'])
@login_required
def addItemViaItemID(item_id, quantity):

    cart_item = db.session.query(CartItem).filter(CartItem.id == item_id).first()

    cart_item.quantity += quantity
    db.session.commit()

    item = cart_item.to_dict()

    product = db.session.query(Product).filter(Product.id == item['product_id']).first()
    images = db.session.query(ProductImage).filter(ProductImage.product_id == item['product_id'])
    owner = db.session.query(User).filter(User.id == product.owner_id).first()

    #add product and images to item
    item['product'] = product.to_dict()
    item['images'] = [image.to_dict() for image in images] #should maybe just get the first image
    item['owner'] = owner.to_dict()

    return {'cart_item': item}, 201



#Delete item (regardless of quantity)
@cart_route.route('/delete/<int:item_id>', methods=['DELETE'])
def deleteItem(item_id):

    cart_item = db.session.query(CartItem).filter(CartItem.id == item_id).first()

    db.session.delete(cart_item)
    db.session.commit()
    return {'message': 'Cart item successfuly deleted'}, 200



#Subtract quantity of item via ITEM id. Will auto-delete item if it is 0 quantity
@cart_route.route('/subtract/<int:item_id>/<int:quantity>', methods=['POST', 'DELETE'])
def subtractDeleteItem(item_id, quantity):

    cart_item = db.session.query(CartItem).filter(CartItem.id == item_id).first()

    if request.method == "POST":

            cart_item.quantity = cart_item.quantity - quantity

            if cart_item.quantity <= 0:
                db.session.delete(cart_item)
                db.session.commit()
                return {'message': 'Cart item successfuly deleted'}, 200
            else:
                db.session.commit()
                return {'cart_item': cart_item.to_dict()}


#Add item via PRODUCT id and CART id
@cart_route.route('/add-product/<int:cart_id>/<int:product_id>', methods=['POST'])
@login_required
def addItemViaProductId(cart_id, product_id):

    item = db.session.query(CartItem).filter(CartItem.cart_id == cart_id).filter(CartItem.product_id == product_id).first()
    #Should check if item belongs to user to send an error
    #should check if an item exists
    #should check if the item is already in the shopping cart
    #quantity should be inputed through a form
    #if item already in cart, add +1 to quantity
    if item:
        item.quantity = item.quantity + 1
        try:
            db.session.commit()
            return {'item': item.to_dict()}, 201
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
            return {'new_item': new_item.to_dict()}, 201
        except:
            return {'errors': {'message': 'Could not update add item to cart'}}

#Create new order
@cart_route.route('/orders', methods=['POST'])
@login_required
def createOrder():
    currentUser = current_user.to_dict()
    user_id = currentUser['id']
    order = Order(
        user_id = user_id,
        total = 0
    )
    try:
        db.session.add(order)
        db.session.commit()
        return {'order': order.to_dict()}, 201
    except:
        return {'errors': {'message': 'There was an error creating order'}}

#Add item to order
@cart_route.route('/orders/<int:order_id>/<int:cart_item_id>', methods=['POST'])
@login_required
def addItemOrder(order_id, cart_item_id):

    order = db.session.query(Order).filter(Order.id == order_id).first()
    cart_item = db.session.query(CartItem).filter(CartItem.id == cart_item_id).first()

    new_item = OrderItem(
        order_id = order.id,
        product_id = cart_item.product_id,
        quantity = cart_item.quantity
    )

    try:
        db.session.add(new_item)
        db.session.commit()
        return {'new_item': new_item.to_dict()}, 201
    except:
        return {'errors': {'message': 'There was an error in adding item to order'}}

#GET Order items
@cart_route.route('/orders/<int:order_id>')
@login_required
def getOrder(order_id):
    order = db.session.query(Order).filter(Order.id == order_id).first()

    if not order:
        return {'errors': {'message': 'Cart does not exist'}}, 404

    items = db.session.query(OrderItem).filter(OrderItem.order_id == order_id)
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


    #set total of cart
    order.total = total
    db.session.commit()

    order_dict = order.to_dict()
    order_dict['items'] = items_dict
    order_dict['total'] = total

    return {'order': order_dict}, 200
