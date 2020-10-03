from selenium.webdriver.common.by import By

from pages.productpage import ProductPage


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.PAGE_URL)

    PAGE_URL = "https://rahulshettyacademy.com/angularpractice/"

    # Locators
    SHOP_BUTTON = (By.CSS_SELECTOR, "a[href*='shop']")

    # Objects
    def click_shop_button(self):
        self.driver.find_element(*self.SHOP_BUTTON).click()
        return ProductPage(self.driver)
