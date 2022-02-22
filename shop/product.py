from dataclasses import dataclass


@dataclass
class Product:
    product_name: str
    cat_name: str
    price: float
    identifier: int

    def __str__(self):
        return f"Produkt: {self.product_name}, Kategoria: {self.cat_name},Cena: {self.price}"

    def __eq__(self, other):
        if self.__class__ != other.__class:
            return NotImplemented
        return (self.product_name == other.product_name and
                self.cat_name == other.cat_name and
                self.price == other.price)
