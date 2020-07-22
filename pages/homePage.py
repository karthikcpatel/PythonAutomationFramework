class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.account_click_xPath = "//span[@class='label'][contains(text(),'Account')]"
        self.clickLogout_xPath = "//a[contains(text(),'Log Out')]"

    def clickAccount(self):
        self.driver.find_element_by_xpath(self.account_click_xPath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.clickLogout_xPath).click()
