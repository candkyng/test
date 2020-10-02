import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser name (chrome, firefox or edge")


@pytest.fixture(scope="class")
def setup_driver(request):
    browser = request.config.getoption("--browser")
    base_url = "https://rahulshettyacademy.com/angularpractice/"

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        assert False, f"Unsupported browser {browser}"

    driver.get(base_url)
    driver.implicitly_wait(1)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

