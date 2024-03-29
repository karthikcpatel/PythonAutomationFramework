from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()
        #self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()
        #self.driver.find_element_by_link_text(self.logout_link_linkText).click()