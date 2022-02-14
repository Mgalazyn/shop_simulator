class Product:

    def __init__(self, product_name, cat_name, price):
        self.price = price
        self.cat_name = cat_name
        self.product_name = product_name

    def print_self(self):
        print(f"Produkt: {self.product_name}, Kategoria: {self.cat_name},Cena: {self.price}")

