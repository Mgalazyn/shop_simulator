class Potato:

    def __init__(self, potato_type, size, price_for_kg):
        self.price_for_kg = price_for_kg
        self.size = size
        self.potato_type = potato_type

    def calculate_price(self, quantity):
        return quantity * self.price_for_kg

    def __repr__(self):
        return f"<potato_type={self.potato_type}, size={self.size}, price_for_kg={self.price_for_kg}>"
