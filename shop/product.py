class Product:

    def __init__(self, product_name, cat_name, price):
        self.price = price
        self.cat_name = cat_name
        self.product_name = product_name


def print_product(product):
    print(f"Produkt: {product.product_name}, Kategoria: {product.cat_name},Cena: {product.price}")


