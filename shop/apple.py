class Apple:

    def __init__(self, apple_type, size, price_for_kg):
        self.price_for_kg = price_for_kg
        self.size = size
        self.apple_type = apple_type

    def calculate_sum(self, quantity):
        return quantity * self.price_for_kg
