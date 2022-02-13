from .products import products, update_product_quantity


orders = [
    {
        "product": "chleb",
        "quantity": 10,
        "total_price": 35
    }
]


def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    avaliable_quantity = products[product_name]["quantity"]

    if avaliable_quantity < quantity:
        print('Przekroczona ilosc dostepnych sztuk')
        return None

    total_price = price * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    update_product_quantity(product_name, quantity)
    orders.append(new_order)
    print(orders)
