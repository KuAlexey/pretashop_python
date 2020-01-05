from src.pages.home_page import *
from tests.base_test import BaseTest


class HomePageTest(BaseTest):

    def test_products_price_symbol(self):
        home_page = HomePage()
        home_page.open_home()

        currencies=home_page.currency_symbol.keys()
        for currency_name in currencies:
            header = home_page.header
            header.select_currency(currency_name)
            header_currency = home_page.header.get_currency()
            product_price_info = home_page.body.get_product_price_info()

            for _, price_symbol in product_price_info:
                assert home_page.currency_symbol[header_currency] == price_symbol
