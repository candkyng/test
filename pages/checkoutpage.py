from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    COUNTRY_INPUT = (By.ID, "country")
    COUNTRY_SUGGESTION = (By.CSS_SELECTOR, "div[class='suggestions']")
    AGREE_CONDITION = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary'")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "input[value='Purchase']")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def enter_destination(self, search_text):
        self.driver.find_element(*self.COUNTRY_INPUT).send_keys(search_text)

    def select_destination_from_dropdown(self, destination):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COUNTRY_SUGGESTION))
        xpath = f"//a[text()='{destination}']"
        self.driver.find_element_by_xpath(xpath).click()

    def get_destination(self):
        return self.driver.execute_script('return document.getElementById("country").value')

    def click_agree_condition(self):
        self.driver.find_element(*self.AGREE_CONDITION).click()

    def click_purchase_button(self):
        self.driver.find_element(*self.PURCHASE_BUTTON).click()

    def get_success_text(self):
        return self.driver.find_element(*self.SUCCESS_ALERT).text

