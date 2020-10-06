from locators.locators import HomepageLocators
from pages.basepage import BasePage
from pages.productpage import ProductPage


class Homepage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    PAGE_URL = "https://rahulshettyacademy.com/angularpractice/"

    def goto(self):
        self.driver.get(self.PAGE_URL)
        return self

    def click_home_button(self):
        self.click(HomepageLocators.HOME_BUTTON)
        return self

    def click_shop_button(self):
        self.click(HomepageLocators.SHOP_BUTTON)
        return ProductPage(self.driver)
