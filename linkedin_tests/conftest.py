import pytest
from selenium import webdriver

from config.config import TestData


@pytest.fixture(scope='function')
def init_driver(request):
    driver = None
    browser_type=TestData.BROWSER
    if browser_type.casefold()=="chrome":
        driver = webdriver.Chrome()
    elif browser_type.casefold() == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.delete_all_cookies()
    driver.quit()

