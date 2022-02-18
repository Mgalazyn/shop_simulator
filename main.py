from shop.order import ExpressOrder
from shop.data_generator import generate_order
from shop.discouts import PercentageDiscount, AbsoluteDiscount
from shop.order import Order


def run_example():
    order_elements = generate_order()
    ten_percent_discount = PercentageDiscount(discount_percentage=10)
    hundred_pln_discount = AbsoluteDiscount(discount_value=100)

    no_discout_order = Order(
        first_name='Marcin',
        last_name='Galazyn',
        order_elements=order_elements
    )
    order_with_percentage_discount = Order(
        first_name='Kamil',
        last_name='Zylinski',
        order_elements=order_elements,
        discount_policy=ten_percent_discount
    )
    order_with_absolute_value_discount = Order(
        first_name='Krzysiek',
        last_name='Kalm',
        order_elements=order_elements,
        discount_policy=hundred_pln_discount
    )

    print(no_discout_order)
    print(order_with_percentage_discount)
    print(order_with_absolute_value_discount)


if __name__ == '__main__':
    run_example()
