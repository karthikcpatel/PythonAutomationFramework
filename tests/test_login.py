from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    # @pytest.fixture(scope="session")
    # def test_setup(self):
    #     global driver
    #     driver = webdriver.Chrome(
    #         executable_path="C:/Users/kartikp/PycharmProjects/PythonAutomationFramework/drivers/chromedriver_83.exe")
    #     driver.implicitly_wait(30)
    #     driver.maximize_window()
    #     yield
    #     driver.close()
    #     print("Test completed successfully")

    def test_login(self,test_setup):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.beforeLogin()
        login.clickLoginLink()
        login.enterUsername(utils.USERNAME)
        login.enterPassword(utils.PASSWORD)
        login.clickLogin()
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        testName = utils.whoami()
        screenshotName = testName+"_"+currTime
        driver.get_screenshot_as_file("C:/Users/kartikp/PycharmProjects/PythonAutomationFramework/screenshots"+ screenshotName +".png")

        # driver.find_element_by_xpath("(//span[@class='label'])[3]").click()
        # driver.find_element_by_xpath("//a[contains(text(),'Log In')]").click()
        # driver.find_element_by_xpath("//input[@id='email']").send_keys("testerkittu@gmail.com")
        # driver.find_element_by_xpath("//input[@id='pass']").send_keys("Netweb@123")
        # driver.find_element_by_xpath("//button[@id='send2']").click()

    def test_logout(self,test_setup):
        try:
            driver = self.driver
            home = HomePage(driver)
            home.clickAccount()
            home.clickLogout()
            pageTitle = driver.title()
            print(pageTitle)
            assert pageTitle == "Customer Login"
            #driver.get_screenshot_as_file("C:/Users/kartikp/PycharmProjects/PythonAutomationFramework/screenshots" + self.screenshotName + ".png")
            # driver.find_element_by_xpath("//span[@class='label'][contains(text(),'Account')]").click()
            # driver.find_element_by_xpath("//a[contains(text(),'Log Out')]").click()
        except:
            print("Unable to get title of the page")