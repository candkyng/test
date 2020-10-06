from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc, element=None):
        if element is None:
            element = self.driver
        WebDriverWait(element, 10).until(EC.presence_of_element_located(loc)).click()




