from logic.orders import create_new_order


def run_shop():
    print('Witaj w sklepie')
    product_name = input('Jaki towar chcesz kupic?: ')
    quantity = int(input('Ile sztuk chcesz kupic?: '))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result['total_price']
        print(f"laczny koszt zamowienia to: {total_price} PLN")


if __name__ == '__main__':
    run_shop()
