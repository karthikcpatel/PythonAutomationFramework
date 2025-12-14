from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.profile_xpath = "//img[@alt='profile picture']//following-sibling::p"
        self.logout_xpath = "//a[text()='Logout']"

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self.profile_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()