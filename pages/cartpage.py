from collections import namedtuple

from selenium.webdriver.common.by import By

from data.shop_data import ShopData
from pages.basepage import BasePage
from pages.checkoutpage import CheckoutPage


class CartPage(BasePage):

    # Locators
    PRODUCT_ROWS = (By.XPATH, "//td[contains(@class,'col-sm-8')]/parent::tr")
    PRODUCT_NAME_IN_ROW = (By.CSS_SELECTOR, "h4 a")
    PRODUCT_TOTAL_IN_ROW = (By.XPATH, "td[4]/strong")
    SUM_OF_TOTAL = (By.XPATH, "//td[@class='text-right']/h3/strong")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[class*='btn-success']")

    product = namedtuple('Product', ['name', 'total'])

    def __init__(self, driver):

        self.driver = driver

    # return a list of tuples with product name and its total amount
    def get_products(self):

        rows = self.get_rows()
        products = []
        for row in rows:
            name = row.find_element(*CartPage.PRODUCT_NAME_IN_ROW).text
            product_total_text = str(row.find_element(*CartPage.PRODUCT_TOTAL_IN_ROW).text)
            product_total_text = product_total_text.replace(ShopData.CURRENCY, "")
            total = float(product_total_text)
            products.append(self.product(name, total))
        return products

    def get_rows(self):

        return self.driver.find_elements(*CartPage.PRODUCT_ROWS)

    def get_total(self):
        total_text = self.driver.find_element(*CartPage.SUM_OF_TOTAL).text
        total_text = total_text.replace(ShopData.CURRENCY, "")
        return float(total_text)

    def click_checkout_button(self):

        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)