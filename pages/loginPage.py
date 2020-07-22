class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.beforeLogin_xPath = "(//span[@class='label'])[3]"
        self.login_link_xPath = "//a[contains(text(),'Log In')]"
        self.username_xPath = "//input[@id='email']"
        self.password_xPath = "//input[@id='pass']"
        self.login_xPath = "//button[@id='send2']"

    def beforeLogin(self):
        self.driver.find_element_by_xpath(self.beforeLogin_xPath).click()

    def clickLoginLink(self):
        self.driver.find_element_by_xpath(self.login_link_xPath).click()

    def enterUsername(self,username):
        self.driver.find_element_by_xpath(self.username_xPath).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element_by_xpath(self.password_xPath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_xPath).click()