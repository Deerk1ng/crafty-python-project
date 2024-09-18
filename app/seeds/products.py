from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text

# not sure which way we would like to


# def seed_products():
#     testProduct1 = Product( owner_id='1' ,name='testProduct1' , price='100.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='mens' )
#     testProduct2 = Product( owner_id='1' ,name='testProduct2' , price='5.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='mens' )
#     testProduct3 = Product( owner_id='1' ,name='testProduct3' , price='19.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct4 = Product( owner_id='2' ,name='testProduct4' , price='37.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='melee' )
#     testProduct5 = Product( owner_id='2' ,name='testProduct5' , price='28.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='melee' )

#     testProduct6 = Product( owner_id='2' ,name='testProduct6' , price='3.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct7 = Product( owner_id='3' ,name='testProduct7' , price='83.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct8 = Product( owner_id='3' ,name='testProduct8' , price='71.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct9 = Product( owner_id='3' ,name='testProduct9' , price='932.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='long-range' )
#     testProduct10 = Product( owner_id='4' ,name='testProduct10' , price='28.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )


#     testProduct11 = Product( owner_id='5' ,name='testProduct11' , price='77.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='long-range' )
#     testProduct12 = Product( owner_id='5' ,name='testProduct12' , price='39.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )
#     testProduct13 = Product( owner_id='5' ,name='testProduct13' , price='27.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='long-range' )
#     testProduct14 = Product( owner_id='1' ,name='testProduct14' , price='9.67' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )
#     testProduct15 = Product( owner_id='1' ,name='testProduct15' , price='1000.50' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )


#     db.session.add([testProduct1, testProduct2, testProduct3, testProduct4, testProduct5, testProduct6, testProduct7, testProduct8, testProduct9, testProduct10, testProduct11, testProduct12, testProduct13, testProduct14, testProduct15])
def seed_products():
    products = {
        "Men's Genuine Leather Medival Belt": {"owner_id": 1, "price": 140.00, "description": "Elevate your historical ensemble with our Medieval Men's Belt, a perfect fusion of functionality and authentic medieval craftsmanship. Designed for those who appreciate the finer details of historical attire, this belt offers a rugged yet refined addition to any medieval or fantasy wardrobe.", "category": 'mens'},
        "Ranger's Cloak": {"owner_id": 5, "price": 75.00, "description": "Step into the heart of adventure with our Ranger's Cloak, a masterfully crafted garment designed for the modern explorer and fantasy enthusiast. Combining practical functionality with an air of mystique, this cloak is an essential companion for those who roam the wilds or seek to embody the spirit of legendary rangers.", "category": 'mens'},
        "Men's Genuine Wool Tunic": {"owner_id": 5, "price": 34.90, "description": "Discover timeless style and unparalleled comfort with our Men's Tunic, a versatile garment that seamlessly blends historical charm with modern practicality. Whether you're attending a medieval reenactment, a renaissance fair, or simply looking to enhance your everyday wardrobe, this tunic is designed to make a statement.", "category": 'mens'},
        "Longsword": {"owner_id": 5, "price": 140.00, "description": "Command respect and exude strength with our Longsword, a masterfully crafted weapon that blends historical accuracy with exceptional functionality. Designed for collectors, reenactors, and martial artists alike, this long sword is a testament to both form and function, ensuring you stand out in any setting.", "category": 'melee'},
        "Dagger": {"owner_id": 5, "price": 28.00, "description": "Unveil the elegance and utility of our meticulously crafted Dagger, a versatile tool designed for both collectors and practitioners. Whether you're enhancing your historical reenactment gear, embarking on a role-playing adventure, or simply appreciating fine craftsmanship, this dagger stands as a testament to timeless design and functionality.", "category": 'melee'},
        "Medival Dress": {"owner_id": 5, "price": 90.00, "description": "Step into a world of timeless elegance with our Women's Medieval Dress, a stunning garment designed to capture the essence of historic beauty and sophistication. Perfect for reenactments, renaissance fairs, or themed events, this dress seamlessly blends authentic medieval design with modern comfort.", "category": 'womens'},
        "Elven Cuffs": {"owner_id": 5, "price": 14.90, "description": 'Unleash your inner elf with our exquisite Elven Cuffs, a beautifully crafted accessory that embodies the grace and elegance of elven craftsmanship. Perfect for fantasy enthusiasts, LARP events, or renaissance fairs, these cuffs add a touch of ethereal charm to any outfit.', "category": 'womens'},
        "Elven Purse": {"owner_id": 5, "price": 29.50, "description": "Inspired by the ethereal beauty of elven craftsmanship, the purse features delicate, nature-inspired motifs, such as intricately embossed leaf patterns and graceful vine designs. The ornate detailing creates a sense of enchantment, capturing the essence of elven elegance.", "category": 'womens'},
        "Viking Throwing Axe": {"owner_id": 6, "price": 132.00, "description": "The Viking Throwing Axe features a classic, battle-hardened design inspired by historical Viking weaponry. Its robust head, often adorned with Norse runes or intricate engravings, reflects the iconic style of Viking axes used in combat and ceremonial practices.", "category": 'long-range'},
        "Medival Mace": {"owner_id": 6, "price": 28.00, "description": "Unleash unparalleled power and authority with our Medieval Mace, a formidable weapon that epitomizes strength and craftsmanship. Designed for reenactors, collectors, and historical enthusiasts, this mace combines historical accuracy with exceptional functionality, making it a standout piece in any medieval armory.", "category": 'melee'},
        "Archer's Bow and Arrows Set": {"owner_id": 6, "price": 77.50, "description": "Step into a realm of fantasy and precision with our Elven Bow and Arrow Set, a masterfully crafted weaponry ensemble designed to captivate and perform. Whether you're a seasoned archer, a fantasy enthusiast, or preparing for a themed event, this set combines elegant craftsmanship with exceptional functionality, transporting you to an enchanting world.", "category": 'long-range'},
        "Mana Vials": {"owner_id": 6, "price": 19.00, "description": "Unlock the magic of your fantasy adventures with our exquisitely crafted Mana Vials, an essential accessory for role-players, collectors, and fantasy enthusiasts. Designed to capture the essence of magical potency, these vials are perfect for adding an element of mystique to your cosplay, LARPing events, or display collection.", "category": 'accessories'},
        "The Judge's Crossbow": {"owner_id": 6, "price": 64.00, "description": "Command authority and precision with the Judge's Crossbow, a meticulously crafted weapon that combines historical elegance with formidable power. Designed for collectors, reenactors, and enthusiasts, this crossbow stands as a symbol of medieval might and judicial gravitas, offering both impressive functionality and aesthetic appeal.", "category": 'long-range'},
        "Viking Shield": {"owner_id": 6, "price": 139.90, "description": "Command the battlefield and showcase your warrior spirit with our Viking Shield, a robust and meticulously crafted piece designed to embody the strength and valor of Viking warriors. Perfect for historical reenactments, fantasy events, or as a striking display item, this shield combines historical authenticity with impressive functionality.", "category": 'accessories'},
        "Ranger's Genuine Leather Boots": {"owner_id": 6, "price": 149.90, "description": "Crafted from premium leather or high-performance synthetic materials, Ranger's Boots are designed to endure the demands of the wild. The sturdy, weather-resistant construction ensures longevity and protection in various conditions, from rugged trails to urban environments.", "category": 'accessories'}
    }

    for name, attributes in products.items():
        product = Product(name=name, **attributes)
        db.session.add(product)

    db.session.commit()


def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
