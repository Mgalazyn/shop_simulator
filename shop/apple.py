from dataclasses import dataclass


@dataclass
class Apple:
    apple_type: str
    size: str
    price_for_kg: float

    def calculate_sum(self, quantity):
        return quantity * self.price_for_kg
