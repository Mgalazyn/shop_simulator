from shop.apple import Apple
from shop.order import print_order, generate_order
from shop.potato import Potato


def run_example():
    small_apple = Apple(apple_type='small', size='S', price_for_kg=5.0)
    big_apple = Apple(apple_type='big', size='L', price_for_kg=6.5)
    print(small_apple.apple_type, small_apple)
    print(big_apple.apple_type, big_apple)

    yellow_potato = Potato(potato_type='yellow', size='S', price_for_kg=1.25)
    print(yellow_potato.potato_type, yellow_potato)

    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)


if __name__ == '__main__':
    run_example()
