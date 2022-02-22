from dataclasses import dataclass


@dataclass
class Potato:
    potato_type: str
    size: str
    price_for_kg: float

    def calculate_price(self, quantity):
        return quantity * self.price_for_kg
