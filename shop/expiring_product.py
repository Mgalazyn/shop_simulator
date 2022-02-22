from shop.product import Product
from dataclasses import dataclass


@dataclass()
class Bestbefore(Product):
    production_date: int
    years_left: int

    def does_expire(self, current_year):
        if (self.production_date + self.years_left) > current_year:
            print('Produkt zdatny do spożycia')
        else:
            print('PRZETERMINOWANYYY!!!')

