from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text

# not sure which way we would like to


# def seed_products():
#     testProduct1 = Product( ownerId='1' ,name='testProduct1' , price='100.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='mens' )
#     testProduct2 = Product( ownerId='1' ,name='testProduct2' , price='5.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='mens' )
#     testProduct3 = Product( ownerId='1' ,name='testProduct3' , price='19.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct4 = Product( ownerId='2' ,name='testProduct4' , price='37.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='melee' )
#     testProduct5 = Product( ownerId='2' ,name='testProduct5' , price='28.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='melee' )

#     testProduct6 = Product( ownerId='2' ,name='testProduct6' , price='3.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct7 = Product( ownerId='3' ,name='testProduct7' , price='83.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct8 = Product( ownerId='3' ,name='testProduct8' , price='71.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='womens' )
#     testProduct9 = Product( ownerId='3' ,name='testProduct9' , price='932.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='long-range' )
#     testProduct10 = Product( ownerId='4' ,name='testProduct10' , price='28.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )


#     testProduct11 = Product( ownerId='5' ,name='testProduct11' , price='77.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='long-range' )
#     testProduct12 = Product( ownerId='5' ,name='testProduct12' , price='39.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )
#     testProduct13 = Product( ownerId='5' ,name='testProduct13' , price='27.00' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='long-range' )
#     testProduct14 = Product( ownerId='1' ,name='testProduct14' , price='9.67' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )
#     testProduct15 = Product( ownerId='1' ,name='testProduct15' , price='1000.50' , description='Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam. ' , category='accessories' )


#     db.session.add([testProduct1, testProduct2, testProduct3, testProduct4, testProduct5, testProduct6, testProduct7, testProduct8, testProduct9, testProduct10, testProduct11, testProduct12, testProduct13, testProduct14, testProduct15])
def seed_products():
    products = {
        "testProduct1": {"ownerId": 1, "price": 100.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'mens'},
        "testProduct2": {"ownerId": 5, "price": 5.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'mens'},
        "testProduct3": {"ownerId": 5, "price": 19.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'womens'},
        "testProduct4": {"ownerId": 5, "price": 37.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'melee'},
        "testProduct5": {"ownerId": 5, "price": 28.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'melee'},
        "testProduct6": {"ownerId": 5, "price": 3.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'womens'},
        "testProduct7": {"ownerId": 5, "price": 83.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'womens'},
        "testProduct8": {"ownerId": 5, "price": 71.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'womens'},
        "testProduct9": {"ownerId": 6, "price": 932.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'long-range'},
        "testProduct10": {"ownerId": 6, "price": 28.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'accessories'},
        "testProduct11": {"ownerId": 6, "price": 77.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'long-range'},
        "testProduct12": {"ownerId": 6, "price": 39.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'accessories'},
        "testProduct13": {"ownerId": 6, "price": 27.00, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'long-range'},
        "testProduct14": {"ownerId": 6, "price": 9.62, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'accessories'},
        "testProduct15": {"ownerId": 6, "price": 1000.50, "description": 'Lorem ipsum odor amet, consectetuer adipiscing elit. Vestibulum conubia odio tempor nisl vestibulum molestie. Ac neque bibendum condimentum interdum a fames euismod nam.', "category": 'accessories'}
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
