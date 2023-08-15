import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)


    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver