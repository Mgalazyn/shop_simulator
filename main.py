from shop.apple import Apple
from shop.potato import Potato
from shop.product import Product
from shop.expiring_product import Bestbefore
from shop.data_generator import generate_order


def run_example():
    grenn_apple = Apple(apple_type='Antonowka',size='XL', price_for_kg=3.5)
    small_potato = Potato(potato_type='Zolty', size='XL', price_for_kg=42.3)
    print(grenn_apple)
    print(small_potato)
    print(grenn_apple.apple_type)

    something = Product(product_name='Ciastko', cat_name='Jedzenie',price=3.52, identifier=201)
    print(something)
    expiring = Bestbefore(product_name='Ciasto', cat_name='Jedzenie', price=30.2, identifier=201,
                          production_date=2021, years_left=3)
    print(expiring)

    produkty = generate_order()
    print(produkty)


if __name__ == '__main__':
    run_example()