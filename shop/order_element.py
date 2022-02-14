class OrderElement:

    def __init__(self, product, quantity):
        self.quantity = quantity
        self.product = product

    def calculate_element_price(self):
        return self.product.price * self.quantity

    def print_self(self):
        self.product.print_self()
        print(f"\t\t x {self.quantity}")