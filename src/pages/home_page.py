from src.pages.base_page import *


class HomePage(BasePage):
    currency_symbol = {'UAH': '₴', 'USD': '$', 'EUR': 'asd'}

    def __init__(self):
        self.header = Header()
        self.body = Body()

    def open_home(self):
        self.open(BASE_URL)


class Header(BasePage):
    def __init__(self):
        self.wait_visible((By.CSS_SELECTOR, 'header'))

    def get_currency(self):
        return self.driver.find_element_by_css_selector("#id_currency~strong").text

    def select_currency(self, currency_shortname):
        log(INFO, f'Select currency {currency_shortname}')
        pass


class Body(BasePage):
    def __init__(self):
        self.wait_visible((By.CSS_SELECTOR, 'body'))

    def _get_products_elements(self):
        return self.wait_any_visible((By.CSS_SELECTOR, "ul[class*=active] .product-container"))

    _product_price_info = []
    _logs = []  # collect product logs

    def get_product_price_info(self) -> List[tuple]:
        for product in self._get_products_elements():
            content_name = self.inner_html(product.find_element_by_css_selector("span[itemprop='name']"))  # TODO
            content_price = self.inner_html(product.find_element_by_css_selector("span[itemprop='price']"))
            split_content_price = [content.strip() for content in content_price.split(' ')]
            price, symbol = split_content_price[0], split_content_price[1]
            self._product_price_info.append((price, symbol))
            self._logs.append(f'For product={content_name} price={price} {symbol}')

        log(INFO, '\n'.join(self._logs))
        return self._product_price_info
