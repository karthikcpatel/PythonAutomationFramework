from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_xpath = "//button[@type='submit']"

    def enter_username(self, username):
        element = self.driver.find_element(By.NAME, self.username_textbox_name)
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.driver.find_element(By.NAME, self.password_textbox_name)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
