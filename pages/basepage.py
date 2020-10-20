from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc, element=None):
        if element is None:
            element = self.driver
        WebDriverWait(element, 10).until(EC.presence_of_element_located(loc)).click()

    def enter_text(self, loc, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc)).send_keys(text)

    def get_text_from_input(self, loc):

        if loc[0] == By.NAME:
            text = self.driver.execute_script(f'return document.getElementsByName("{loc[1]}")[0].value')

        elif loc[0] == By.ID:
            text = self.driver.execute_script(f'return document.getElementById("{loc[1]}").value')

        return text
