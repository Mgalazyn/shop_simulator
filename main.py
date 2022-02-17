from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
from shop.tax_calculator import TaxCalculator
from shop.data_generator import generate_order
from shop.expiring_product import Bestbefore


def run_example():
    food = Bestbefore(
        product_name='serek wiejski',
        cat_name='jedzenie',
        price=10,
        production_date=2021,
        years_left=3
    )
    print(food.does_expire(2022))


if __name__ == '__main__':
    run_example()
