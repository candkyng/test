from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def click(self, loc):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc)).click()
