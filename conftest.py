import pytest
from logging import INFO, log
from selenium import webdriver

from src.pages.base_page import BasePage
from util.utils import *


@pytest.fixture(scope="class")
def setup_driver(request):
    web_driver = webdriver.Chrome(executable_path=resources_file('chromedriver.exe'))
    web_driver.maximize_window()

    BasePage.driver = web_driver
    request.cls.driver = web_driver

    log(INFO, 'Driver is initialized')
    yield
    web_driver.close()
    log(INFO, 'Driver is closed')
