import random
from shop.product import Product
from shop.order_element import OrderElement


class Order:

    MAX_ORDER_ELEMENTS = 5

    def __init__(self, first_name, last_name, order_elements=None):
        self.last_name = last_name
        self.first_name = first_name
        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS:
            order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS]
        self._order_elements = order_elements


    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_element_price()
        return total_price

    def add_product_to_order(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)
        else:
            print('Osiagniete limit pozycji w zamowieniu')

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) < Order.MAX_ORDER_ELEMENTS:
            self._order_elements = value
        else:
            print('Za dużo elementów w zamówieniu')
            self._order_elements = value[:Order.MAX_ORDER_ELEMENTS]


    def __str__(self):
        order_details = f"Zamowienie zlozone przez: {self.first_name} {self.last_name}"
        value_details = f"Wartosc zmaowniea to: {self.total_price} zl"
        product_details = 'Zamowione produkty: '
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([order_details, value_details, product_details])
        return result

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self._order_elements) != len(other.order_elements):
            return False

        if self.first_name != other.first_name or self.last_name != other.last_name:
            return False

        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False
        return True

    def __len__(self):
        return len(self._order_elements)

    @classmethod
    def generate_order(cls):
        number_of_product = random.randint(5, cls.MAX_ORDER_ELEMENTS)
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
