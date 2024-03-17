from selenium.webdriver.common.by import By

from linkedin_webpages.BasePage import BasePage


class LoginPage(BasePage):
    email = (By.ID, "session_key")
    password = (By.ID, "session_password")
    loginBtn = (By.XPATH, "//button[contains(text(),'Sign in')]")

    def __init__(self, driver):
        super().__init__(driver)

    def load_url(self, url):
        self.driver.get(url)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin()

    def enter_email(self, value):
        self.setText(self.email, value)

    def enter_password(self, value):
        self.setText(self.password, value)

    def click_signin(self):
        assert self.click(self.loginBtn)
