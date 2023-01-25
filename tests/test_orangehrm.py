import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        """This function will perform the login operation.
        """
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        """This function will click on logout button on home page.
        """
        try:
            #driver = self.driver
            homepage = HomePage(self.driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = self.driver.title
            assert x == "OrangeHRM"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            #The below code will take screenshot with current timestamp
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            #The below code will generate allure reports
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("C:\\Users\\kartik.patel\\PycharmProjects\\PythonAutomationFramework\\screenshots\\"+ screenshotName +".png")

            raise
        except:
            print("There was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "C:\\Users\\kartik.patel\\PycharmProjects\\PythonAutomationFramework\\screenshots\\"+ screenshotName +".png")

            raise
        else:
            print("No exceptions occurred")
        finally:
            print("I am inside finally block")
            print("This is Sandesh")


