from app.models import db, ProductImage, environment, SCHEMA
from sqlalchemy.sql import text


def seed_product_images():
    product_images = {
        "productImage1": {'url': 'http://example.com/images/product_1_image_1.jpg', 'preview': True, 'productId': 1},
        "productImage2": {'url': 'http://example.com/images/product_1_image_2.jpg', 'preview': True, 'productId': 1},
        "productImage3": {'url': 'http://example.com/images/product_1_image_3.jpg', 'preview': True, 'productId': 1},
        "productImage4": {'url': 'http://example.com/images/product_1_image_4.jpg', 'preview': True, 'productId': 1},
        "productImage5": {'url': 'http://example.com/images/product_1_image_5.jpg', 'preview': True, 'productId': 1},

        "productImage6": {'url': 'http://example.com/images/product_2_image_1.jpg', 'preview': True, 'productId': 2},
        "productImage7": {'url': 'http://example.com/images/product_2_image_2.jpg', 'preview': True, 'productId': 2},
        "productImage8": {'url': 'http://example.com/images/product_2_image_3.jpg', 'preview': True, 'productId': 2},
        "productImage9": {'url': 'http://example.com/images/product_2_image_4.jpg', 'preview': True, 'productId': 2},
        "productImage10": {'url': 'http://example.com/images/product_2_image_5.jpg', 'preview': True, 'productId': 2},

        "productImage11": {'url': 'http://example.com/images/product_3_image_1.jpg', 'preview': True, 'productId': 3},
        "productImage12": {'url': 'http://example.com/images/product_3_image_2.jpg', 'preview': True, 'productId': 3},
        "productImage13": {'url': 'http://example.com/images/product_3_image_3.jpg', 'preview': True, 'productId': 3},
        "productImage14": {'url': 'http://example.com/images/product_3_image_4.jpg', 'preview': True, 'productId': 3},
        "productImage15": {'url': 'http://example.com/images/product_3_image_5.jpg', 'preview': True, 'productId': 3},

        "productImage16": {'url': 'http://example.com/images/product_4_image_1.jpg', 'preview': True, 'productId': 4},
        "productImage17": {'url': 'http://example.com/images/product_4_image_2.jpg', 'preview': True, 'productId': 4},
        "productImage18": {'url': 'http://example.com/images/product_4_image_3.jpg', 'preview': True, 'productId': 4},
        "productImage19": {'url': 'http://example.com/images/product_4_image_4.jpg', 'preview': True, 'productId': 4},
        "productImage20": {'url': 'http://example.com/images/product_4_image_5.jpg', 'preview': True, 'productId': 4},

        "productImage21": {'url': 'http://example.com/images/product_5_image_1.jpg', 'preview': True, 'productId': 5},
        "productImage22": {'url': 'http://example.com/images/product_5_image_2.jpg', 'preview': True, 'productId': 5},
        "productImage23": {'url': 'http://example.com/images/product_5_image_3.jpg', 'preview': True, 'productId': 5},
        "productImage24": {'url': 'http://example.com/images/product_5_image_4.jpg', 'preview': True, 'productId': 5},
        "productImage25": {'url': 'http://example.com/images/product_5_image_5.jpg', 'preview': True, 'productId': 5},

        "productImage26": {'url': 'http://example.com/images/product_6_image_1.jpg', 'preview': True, 'productId': 6},
        "productImage27": {'url': 'http://example.com/images/product_6_image_2.jpg', 'preview': True, 'productId': 6},
        "productImage28": {'url': 'http://example.com/images/product_6_image_3.jpg', 'preview': True, 'productId': 6},
        "productImage29": {'url': 'http://example.com/images/product_6_image_4.jpg', 'preview': True, 'productId': 6},
        "productImage30": {'url': 'http://example.com/images/product_6_image_5.jpg', 'preview': True, 'productId': 6},

        "productImage31": {'url': 'http://example.com/images/product_7_image_1.jpg', 'preview': True, 'productId': 7},
        "productImage32": {'url': 'http://example.com/images/product_7_image_2.jpg', 'preview': True, 'productId': 7},
        "productImage33": {'url': 'http://example.com/images/product_7_image_3.jpg', 'preview': True, 'productId': 7},
        "productImage34": {'url': 'http://example.com/images/product_7_image_4.jpg', 'preview': True, 'productId': 7},
        "productImage35": {'url': 'http://example.com/images/product_7_image_5.jpg', 'preview': True, 'productId': 7},

        "productImage36": {'url': 'http://example.com/images/product_8_image_1.jpg', 'preview': True, 'productId': 8},
        "productImage37": {'url': 'http://example.com/images/product_8_image_2.jpg', 'preview': True, 'productId': 8},
        "productImage38": {'url': 'http://example.com/images/product_8_image_3.jpg', 'preview': True, 'productId': 8},
        "productImage39": {'url': 'http://example.com/images/product_8_image_4.jpg', 'preview': True, 'productId': 8},
        "productImage40": {'url': 'http://example.com/images/product_8_image_5.jpg', 'preview': True, 'productId': 8},

        "productImage41": {'url': 'http://example.com/images/product_9_image_1.jpg', 'preview': True, 'productId': 9},
        "productImage42": {'url': 'http://example.com/images/product_9_image_2.jpg', 'preview': True, 'productId': 9},
        "productImage43": {'url': 'http://example.com/images/product_9_image_3.jpg', 'preview': True, 'productId': 9},
        "productImage44": {'url': 'http://example.com/images/product_9_image_4.jpg', 'preview': True, 'productId': 9},
        "productImage45": {'url': 'http://example.com/images/product_9_image_5.jpg', 'preview': True, 'productId': 9},

        "productImage46": {'url': 'http://example.com/images/product_10_image_1.jpg', 'preview': True, 'productId': 10},
        "productImage47": {'url': 'http://example.com/images/product_10_image_2.jpg', 'preview': True, 'productId': 10},
        "productImage48": {'url': 'http://example.com/images/product_10_image_3.jpg', 'preview': True, 'productId': 10},
        "productImage49": {'url': 'http://example.com/images/product_10_image_4.jpg', 'preview': True, 'productId': 10},
        "productImage50": {'url': 'http://example.com/images/product_10_image_5.jpg', 'preview': True, 'productId': 10},

        "productImage51": {'url': 'http://example.com/images/product_11_image_1.jpg', 'preview': True, 'productId': 11},
        "productImage52": {'url': 'http://example.com/images/product_11_image_2.jpg', 'preview': True, 'productId': 11},
        "productImage53": {'url': 'http://example.com/images/product_11_image_3.jpg', 'preview': True, 'productId': 11},
        "productImage54": {'url': 'http://example.com/images/product_11_image_4.jpg', 'preview': True, 'productId': 11},
        "productImage55": {'url': 'http://example.com/images/product_11_image_5.jpg', 'preview': True, 'productId': 11},

        "productImage56": {'url': 'http://example.com/images/product_12_image_1.jpg', 'preview': True, 'productId': 12},
        "productImage57": {'url': 'http://example.com/images/product_12_image_2.jpg', 'preview': True, 'productId': 12},
        "productImage58": {'url': 'http://example.com/images/product_12_image_3.jpg', 'preview': True, 'productId': 12},
        "productImage59": {'url': 'http://example.com/images/product_12_image_4.jpg', 'preview': True, 'productId': 12},
        "productImage60": {'url': 'http://example.com/images/product_12_image_5.jpg', 'preview': True, 'productId': 12},

        "productImage61": {'url': 'http://example.com/images/product_13_image_1.jpg', 'preview': True, 'productId': 13},
        "productImage62": {'url': 'http://example.com/images/product_13_image_2.jpg', 'preview': True, 'productId': 13},
        "productImage63": {'url': 'http://example.com/images/product_13_image_3.jpg', 'preview': True, 'productId': 13},
        "productImage64": {'url': 'http://example.com/images/product_13_image_4.jpg', 'preview': True, 'productId': 13},
        "productImage65": {'url': 'http://example.com/images/product_13_image_5.jpg', 'preview': True, 'productId': 13},

        "productImage66": {'url': 'http://example.com/images/product_14_image_1.jpg', 'preview': True, 'productId': 14},
        "productImage67": {'url': 'http://example.com/images/product_14_image_2.jpg', 'preview': True, 'productId': 14},
        "productImage68": {'url': 'http://example.com/images/product_14_image_3.jpg', 'preview': True, 'productId': 14},
        "productImage69": {'url': 'http://example.com/images/product_14_image_4.jpg', 'preview': True, 'productId': 14},
        "productImage70": {'url': 'http://example.com/images/product_14_image_5.jpg', 'preview': True, 'productId': 14},

        "productImage71": {'url': 'http://example.com/images/product_15_image_1.jpg', 'preview': True, 'productId': 15},
        "productImage72": {'url': 'http://example.com/images/product_15_image_2.jpg', 'preview': True, 'productId': 15},
        "productImage73": {'url': 'http://example.com/images/product_15_image_3.jpg', 'preview': True, 'productId': 15},
        "productImage74": {'url': 'http://example.com/images/product_15_image_4.jpg', 'preview': True, 'productId': 15},
        "productImage75": {'url': 'http://example.com/images/product_15_image_5.jpg', 'preview': True, 'productId': 15},
    }

    for key, attributes in product_images.items():
        product_image = ProductImage(**attributes)
        db.session.add(product_image)

    db.session.commit()


def undo_productImages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.productImages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM productImages"))

    db.session.commit()
