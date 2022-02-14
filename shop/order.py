import random
from shop.product import Product, print_product


class Order:

    def __init__(self, first_name, last_name, products_list=None):
        self.last_name = last_name
        self.first_name = first_name
        if products_list is None:
            products_list = []
        self.products_list = products_list

        total_price = 0
        for product in products_list:
            total_price += product.price
        self.total_price = total_price


def print_order(order):
    print(f"Zamowienie: {order.first_name}, {order.last_name}")
    print(f"Zamowienie zlozone przez {order.first_name} {order.last_name}")
    print(f"O wartosci: {order.total_price}")
    print('Zamowione produkty')
    for product in order.products_list:
        print("\t", end='')
        print_product(product)


def generate_order():
    number_of_product = random.randint(1, 10)
    products = []
    for product_number in range(number_of_product):
        product_name = f"Produkt {product_number}"
        cat_name = "Inne"
        price = random.randint(1, 50)
        product = Product(product_name, cat_name, price)
        products.append(product)

    order = Order(first_name='Marcin', last_name='Galazyn', products_list=products)
    return order

