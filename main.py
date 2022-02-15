from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
from shop.tax_calculator import TaxCalculator


def run_example():
    cookie = Product(product_name="Ciastko", cat_name="Jedzenie", price=4)
    szpinak = Product(product_name='szpinak', cat_name='Owoce i Warzywa', price=7)
    smth = Product(product_name='cos',cat_name='inne', price=39)
    cookies = OrderElement(cookie, quantity=10)
    piec_szpinaku = OrderElement(szpinak, quantity=5)
    duzo_cos = OrderElement(smth, quantity=2)
    
    cookies_tax = TaxCalculator.tax_for_category(cookies)
    szpinak_tax = TaxCalculator.tax_for_category(piec_szpinaku)
    cos_tax = TaxCalculator.tax_for_category(duzo_cos)

    print(f"Cena ciastek to: {cookies.calculate_element_price()} + {cookies_tax:.2f}")
    print(f"Cena szpinaku to: {piec_szpinaku.calculate_element_price()} + {szpinak_tax:.2f}")
    print(f"Cena czegos to: {duzo_cos.calculate_element_price()} + {cos_tax:.2f}")


if __name__ == '__main__':
    run_example()
