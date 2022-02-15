class OrderElement:

    def __init__(self, product, quantity):
        self.quantity = quantity
        self.product = product

    def calculate_element_price(self):
        return self.product.price * self.quantity

    def __str__(self, other):
        if self.__class__ != other.__class:
            return NotImplemented
        return self.quantity == other.quantity and self.product == other.product

    def __str__(self):
        return f" {self.product} x {self.quantity}"
