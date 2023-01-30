from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "username"
        #self.username_textbox_placeholder = "Username"
        self.password_textbox_name = "password"
        self.login_button_xpath = "//button[@type='submit']"

    def enter_username(self, username):
        """This function will enter username is username textbox.
        """
        self.driver.find_element(By.NAME,self.username_textbox_name).clear
        self.driver.find_element(By.NAME,self.username_textbox_name).send_keys(username)
        #self.driver.find_element_by_name(self.username_textbox_name).clear()
        #self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        """This function will enter password is password textbox.
        """
        self.driver.find_element(By.NAME,self.password_textbox_name).clear
        self.driver.find_element(By.NAME,self.password_textbox_name).send_keys(password)

    def click_login(self):
        """This function will click on login button.
        """
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()