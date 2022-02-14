import random
from shop.product import Product
from shop.order_element import OrderElement


class Order:

    def __init__(self, first_name, last_name, order_elements=None):
        self.last_name = last_name
        self.first_name = first_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.calculate_element_price()
        return total_price

    def print_self(self):
        print(f"Zamowienie: {self.first_name}, {self.last_name}")
        print(f"Zamowienie zostalo zlozone przez {self.first_name} {self.last_name}")
        print(f"Wartosc zamowienia to: {self.total_price} PLN")
        print(f"Zamowione produkty to: ")
        for element in self.order_elements:
            element.print_self()


def generate_order():
    number_of_product = random.randint(1, 10)
    order_elements = []
    for product_number in range(number_of_product):
        product_name = f"Produkt {product_number}"
        cat_name = "Inne"
        price = random.randint(1, 50)
        product = Product(product_name, cat_name, price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product=product, quantity=quantity))
    order = Order(first_name="Marcin", last_name="Galazyn", order_elements=order_elements)
    return order
