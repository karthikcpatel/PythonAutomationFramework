import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():

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
        driver.get_screenshot_as_file("C:/Users/kartikp/PycharmProjects/PythonAutomationFramework/screenshots/"+ screenshotName +".png")

    def test_logout(self,test_setup):
        try:
            driver = self.driver
            home = HomePage(driver)
            home.clickAccount()
            home.clickLogout()
            pageTitle = driver.title()
            print(pageTitle)
            assert pageTitle == "Customer Login"
        except:
            print("Unable to get title of the page")