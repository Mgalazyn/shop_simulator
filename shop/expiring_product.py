from shop.product import Product


class Bestbefore(Product):

    def __init__(self, product_name, cat_name, price, production_date, years_left):
        super().__init__(product_name, cat_name, price)
        self.production_date = production_date
        self.years_left = years_left

    def does_expire(self, current_year):
        if (self.production_date + self.years_left) > current_year:
            print('Produkt zdatny do spożycia')
        else:
            print('PRZETERMINOWANYYY!!!')

