import time
import csv

import pytest

from config.config import TestData
from linkedin_tests.BaseTest import BaseTest
from linkedin_webpages.LoginPage import LoginPage
from config.config import get_excel_data


class TestLogin(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password", csv.reader(open(TestData.filepath)))
    def test_login(self, username: str, password: str):
        self.login_page = LoginPage(self.driver)
        self.login_page.load_url(TestData.BASE_URL)
        self.login_page.login(username, password)
        time.sleep(10)

    @pytest.mark.datadriventests
    @pytest.mark.parametrize("data", get_excel_data(TestData.filepath))
    def test_login(self, data):
        self.login_page = LoginPage(self.driver)
        self.login_page.load_url(TestData.BASE_URL)
        self.login_page.login(data['username'], data['password'])
        time.sleep(10)

    @pytest.mark.Regression
    def test_test2(self):
        pytest.skip("Skipping Test case")
