import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup_driver(request):

    base_url = "https://rahulshettyacademy.com/angularpractice/"

    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.implicitly_wait(1)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
