class Product:

    def __init__(self, product_name, cat_name, price):
        self.price = price
        self.cat_name = cat_name
        self.product_name = product_name

    def __str__(self):
        return f"Produkt: {self.product_name}, Kategoria: {self.cat_name},Cena: {self.price}"

    def __eq__(self, other):
        if self.__class__ != other.__class:
            return NotImplemented
        return (self.product_name == other.product_name and
                self.cat_name == other.cat_name and
                self.price == other.price)
