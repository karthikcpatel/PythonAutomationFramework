from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.profile_link = "//p[text()='manda user']"
        self.logout_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self.profile_link).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()