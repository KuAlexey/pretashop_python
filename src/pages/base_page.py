from typing import List
from logging import INFO, log

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement, By
from selenium.webdriver.support import (wait, expected_conditions as EC)

BASE_URL = 'http://prestashop.qatestlab.com.ua/en/'


# instance of web driver is passed in conftest.py
class BasePage:
    WAIT_SECONDS = 10
    driver: WebDriver = None

    def open(self, url):
        log(INFO, f'Open {url}')
        self.driver.get(url)
        pass

    def wait_for(self, method, timeout=WAIT_SECONDS):
        return wait.WebDriverWait(self.driver, timeout=timeout).until(method)

    def wait_visible(self, searched_object, timeout=WAIT_SECONDS) -> WebElement:
        if isinstance(searched_object, WebElement):
            return self.wait_for(EC.visibility_of(searched_object), timeout)
        if isinstance(searched_object, str):
            return self.wait_for(EC.visibility_of_element_located((By.XPATH, searched_object)), timeout)
        if isinstance(searched_object, tuple):
            return self.wait_for(EC.visibility_of_element_located(searched_object), timeout)

        raise TypeError('Wrong dom_element type, should be str, WebElement or Tuple(By,str)')

    def wait_any_visible(self, searched_object, timeout=WAIT_SECONDS) -> List[WebElement]:
        if isinstance(searched_object, list):
            def any_visible(elements):
                for element in elements:
                    return element.is_displayed()

            self.wait_for(any_visible(searched_object))
            return searched_object

        if isinstance(searched_object, str):
            return self.wait_for(EC.visibility_of_any_elements_located((By.XPATH, searched_object)), timeout)
        if isinstance(searched_object, tuple):
            return self.wait_for(EC.visibility_of_any_elements_located(searched_object), timeout)

        raise TypeError('Wrong dom_element type, should be str, List or Tuple(By,str)')

    def is_present(self, searched_object):
        if isinstance(searched_object, WebElement):
            return bool(searched_object.tag_name)
        if isinstance(searched_object, str):
            return bool(self.driver.find_element_by_xpath(searched_object).tag_name)
        if isinstance(searched_object, tuple):
            by, value = searched_object
            return bool(self.driver.find_element(by, value).tag_name)

        raise TypeError('Wrong dom_element type, should be str, Tuple(By,str)')

    def wait_presence(self, searched_object, timeout=WAIT_SECONDS) -> WebElement:
        self.wait_for(self.is_present(searched_object), timeout)
        return searched_object

    def wait_all_presence(self, searched_object, timeout=WAIT_SECONDS) -> List[WebElement]:
        if isinstance(searched_object, list):
            return [self.wait_presence(element) for element in searched_object]
        if isinstance(searched_object, str):
            return self.wait_for(EC.presence_of_all_elements_located((By.XPATH, searched_object)), timeout)
        if isinstance(searched_object, tuple):
            by, value = searched_object
            return self.wait_for(EC.visibility_of_any_elements_located((by, value)), timeout)

        raise TypeError('Wrong dom_element type, should be str, Tuple(By,str)')

    def inner_html(self, element: WebElement):
        return element.get_attribute("innerHTML")
