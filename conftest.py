import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type browser name:")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path="C:/Users/kartikp/PycharmProjects/PythonAutomationFramework/drivers/chromedriver_86.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:/Users/kartikp/PycharmProjects/PythonAutomationFramework/drivers/geckodriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    print("Test completed successfully")