from shop.order import generate_order
from shop.order import Order


def run_example():
    first_order = generate_order()
    first_order.print_self()
    second_order = generate_order()
    second_order.print_self()


if __name__ == '__main__':
    run_example()
