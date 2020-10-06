from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.productpage import ProductPage


class Homepage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    PAGE_URL = "https://rahulshettyacademy.com/angularpractice/"

    # Locators
    SHOP_BUTTON = (By.CSS_SELECTOR, "a[href*='shop']")
    HOME_BUTTON = (By.LINK_TEXT, "Home")

    def goto(self):
        self.driver.get(self.PAGE_URL)
        return self

    def click_home_button(self):
        self.click(self.HOME_BUTTON)
        return self

    def click_shop_button(self):
        self.click(self.SHOP_BUTTON)
        return ProductPage(self.driver)
