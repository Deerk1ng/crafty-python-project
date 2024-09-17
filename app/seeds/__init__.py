from flask.cli import AppGroup
from .users import seed_users, undo_users
from .products import seed_products, undo_products
from .reviews import seed_reviews, undo_reviews
from .review_images import seed_review_images, undo_review_images
from .orders import seed_orders, undo_orders
from .order_items import seed_order_items, undo_order_items
from .product_images import seed_product_images, undo_product_images


from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_product_images()
        undo_order_items()
        undo_orders()
        undo_review_images()
        undo_reviews()
        undo_products()
        undo_users()


    seed_users()
    # Add other seed functions here
    seed_products()
    seed_product_images()

    seed_reviews()
    seed_review_images()
    seed_orders()
    seed_order_items()


# Creates the `flask seed undo` command
@seed_commands.command('undo') ##might want this to be reverse order?
def undo():
    undo_product_images()
    undo_order_items()
    undo_orders()
    undo_review_images()
    undo_reviews()
    undo_products()
    undo_users()
    # Add other undo functions here
