import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")

@pytest.fixture(scope="class")

def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()