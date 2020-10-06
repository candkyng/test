from selenium.webdriver.common.by import By

from locators.locators import CheckoutPageLocators
from pages.basepage import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def enter_destination(self, search_text):
        self.driver.find_element(*CheckoutPageLocators.COUNTRY_INPUT).send_keys(search_text)

    def select_destination_from_dropdown(self, destination):
        locator = (By.XPATH, f"//a[text()='{destination}']")
        self.click(locator)

    def get_destination(self):
        return self.driver.execute_script('return document.getElementById("country").value')

    def click_agree_condition(self):
        self.driver.find_element(*CheckoutPageLocators.AGREE_CONDITION).click()

    def click_purchase_button(self):
        self.driver.find_element(*CheckoutPageLocators.PURCHASE_BUTTON).click()

    def get_success_text(self):
        return self.driver.find_element(*CheckoutPageLocators.SUCCESS_ALERT).text

