from app.models import db, ProductImage, environment, SCHEMA
from sqlalchemy.sql import text


def seed_product_images():
    product_images = {
        "productImage1": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/belt1.jpg', 'preview': True, 'product_id': 1},
        "productImage2": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/belt2.jpg', 'preview': False, 'product_id': 1},
        "productImage3": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/belt3.jpg', 'preview': False, 'product_id': 1},
        "productImage4": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/belt4.jpg', 'preview': False, 'product_id': 1},
        "productImage5": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/belt5.jpg', 'preview': False, 'product_id': 1},

        "productImage6": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cloak1.jpg', 'preview': True, 'product_id': 2},
        "productImage7": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cloak2.jpg', 'preview': False, 'product_id': 2},
        "productImage8": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cloak3.jpg', 'preview': False, 'product_id': 2},
        "productImage9": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cloak4.jpg', 'preview': False, 'product_id': 2},
        "productImage10": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cloak5.jpg', 'preview': False, 'product_id': 2},

        "productImage11": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/tunic1.jpg', 'preview': True, 'product_id': 3},
        "productImage12": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/tunic2.jpg', 'preview': False, 'product_id': 3},
        "productImage13": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/tunic3.jpg', 'preview': False, 'product_id': 3},
        "productImage14": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/tunic4.jpg', 'preview': False, 'product_id': 3},
        "productImage15": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/tunic5.jpg', 'preview': False, 'product_id': 3},

        "productImage16": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/sword1.jpg', 'preview': True, 'product_id': 4},
        "productImage17": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/sword2.jpg', 'preview': False, 'product_id': 4},
        "productImage18": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/sword3.jpg', 'preview': False, 'product_id': 4},
        "productImage19": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/sword4.jpg', 'preview': False, 'product_id': 4},
        "productImage20": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/sword5.jpg', 'preview': False, 'product_id': 4},

        "productImage21": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dagger1.jpg', 'preview': True, 'product_id': 5},
        "productImage22": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dagger2.jpg', 'preview': False, 'product_id': 5},
        "productImage23": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dagger3.jpg', 'preview': False, 'product_id': 5},
        "productImage24": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dagger4.jpg', 'preview': False, 'product_id': 5},
        "productImage25": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dagger5.jpg', 'preview': False, 'product_id': 5},

        "productImage26": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dress1.jpg', 'preview': True, 'product_id': 6},
        "productImage27": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dress2.jpg', 'preview': False, 'product_id': 6},
        "productImage28": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dress3.jpg', 'preview': False, 'product_id': 6},
        "productImage29": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dress4.jpg', 'preview': False, 'product_id': 6},
        "productImage30": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/dress5.jpg', 'preview': False, 'product_id': 6},

        "productImage31": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cuffs1.jpg', 'preview': True, 'product_id': 7},
        "productImage32": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cuffs2.jpg', 'preview': False, 'product_id': 7},
        "productImage33": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cuffs3.jpg', 'preview': False, 'product_id': 7},
        "productImage34": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cuffs4.jpg', 'preview': False, 'product_id': 7},
        "productImage35": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/cuffs5.jpg', 'preview': False, 'product_id': 7},

        "productImage36": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/purse1.jpg', 'preview': True, 'product_id': 8},
        "productImage37": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/purse2.jpg', 'preview': False, 'product_id': 8},
        "productImage38": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/purse3.jpg', 'preview': False, 'product_id': 8},
        "productImage39": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/purse4.jpg', 'preview': False, 'product_id': 8},
        "productImage40": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/purse5.jpg', 'preview': False, 'product_id': 8},

        "productImage41": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/axe1.jpg', 'preview': True, 'product_id': 9},
        "productImage42": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/axe2.jpg', 'preview': False, 'product_id': 9},
        "productImage43": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/axe3.jpg', 'preview': False, 'product_id': 9},
        "productImage44": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/axe4.jpg', 'preview': False, 'product_id': 9},
        "productImage45": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/axe5.jpg', 'preview': False, 'product_id': 9},

        "productImage46": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mace1.jpg', 'preview': True, 'product_id': 10},
        "productImage47": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mace2.jpg', 'preview': False, 'product_id': 10},
        "productImage48": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mace3.jpg', 'preview': False, 'product_id': 10},
        "productImage49": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mace4.jpg', 'preview': False, 'product_id': 10},
        "productImage50": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mace5.jpg', 'preview': False, 'product_id': 10},

        "productImage51": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/bow1.jpg', 'preview': True, 'product_id': 11},
        "productImage52": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/bow2.jpg', 'preview': False, 'product_id': 11},
        "productImage53": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/bow3.jpg', 'preview': False, 'product_id': 11},
        "productImage54": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/bow4.jpg', 'preview': False, 'product_id': 11},
        "productImage55": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/bow5.jpg', 'preview': False, 'product_id': 11},

        "productImage56": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mana1.jpg', 'preview': True, 'product_id': 12},
        "productImage57": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mana2.jpg', 'preview': False, 'product_id': 12},
        "productImage58": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mana3.jpg', 'preview': False, 'product_id': 12},
        "productImage59": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mana4.jpg', 'preview': False, 'product_id': 12},
        "productImage60": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/mana5.jpg', 'preview': False, 'product_id': 12},

        "productImage61": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/crossbow1.jpg', 'preview': True, 'product_id': 13},
        "productImage62": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/crossbow2.jpg', 'preview': False, 'product_id': 13},
        "productImage63": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/crossbow3.jpg', 'preview': False, 'product_id': 13},
        "productImage64": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/crossbow4.jpg', 'preview': False, 'product_id': 13},
        "productImage65": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/crossbow5.jpg', 'preview': False, 'product_id': 13},

        "productImage66": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/shield1.jpg', 'preview': True, 'product_id': 14},
        "productImage67": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/shield2.jpg', 'preview': False, 'product_id': 14},
        "productImage68": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/shield3.jpg', 'preview': False, 'product_id': 14},
        "productImage69": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/shield4.jpg', 'preview': False, 'product_id': 14},
        "productImage70": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/shield5.jpg', 'preview': False, 'product_id': 14},

        "productImage71": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/boots1.jpg', 'preview': True, 'product_id': 15},
        "productImage72": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/boots2.jpg', 'preview': False, 'product_id': 15},
        "productImage73": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/boots3.jpg', 'preview': False, 'product_id': 15},
        "productImage74": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/boots4.jpg', 'preview': False, 'product_id': 15},
        "productImage75": {'url': 'https://craftyproject.s3.us-east-2.amazonaws.com/boots5.jpg', 'preview': False, 'product_id': 15},
    }

    for key, attributes in product_images.items():
        product_image = ProductImage(**attributes)
        db.session.add(product_image)

    db.session.commit()


def undo_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM product_images"))

    db.session.commit()
