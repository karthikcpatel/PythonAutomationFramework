from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.username = {
            "primary": (By.NAME, "username"),
            "fallbacks": [
                (By.XPATH, "//input[@placeholder='Username']"),
                (By.CSS_SELECTOR, "input[type='text']")
            ]
        }


        self.password = {
            "primary": (By.NAME, "password"),
            "fallbacks": [
                (By.XPATH, "//input[@type='password']")
            ]
        }

        self.login_button = {
            "primary": (By.XPATH, "//button[@type='submit']"),
            "fallbacks": [
                (By.XPATH, "//button[contains(.,'Login')]"),
                (By.CSS_SELECTOR, "button.oxd-button")
            ]
        }

    def enter_username(self, username):
        el = self.find("username", self.username)
        el.clear()
        el.send_keys(username)

    def enter_password(self, password):
        el = self.find("password", self.password)
        el.clear()
        el.send_keys(password)

    def click_login(self):
        self.find("login_button", self.login_button).click()
