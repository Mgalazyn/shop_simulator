products = {
    'chleb': {
        "quantity": 100,
        "price": 3.5
    },
    'jablka': {
        "quantity": 50,
        "price": 5.5
    }
}


def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity