class TaxRates:

    FRUITS_AND_VEGE = 0.05
    FOOD = 0.08
    ALL = 0.2


class TaxCalculator:

    @staticmethod
    def tax_for_category(order_element):
        product_category = order_element.product.cat_name
        if product_category == 'Owoce i Warzywa':
            tax_rate = TaxRates.FRUITS_AND_VEGE
        elif product_category == 'Jedzenie':
            tax_rate = TaxRates.FOOD
        else:
            tax_rate = TaxRates.ALL
        return tax_rate * order_element.calculate_element_price()
