from collections import namedtuple

from data.shop_data import ShopData
from locators.locators import CartPageLocators
from pages.basepage import BasePage
from pages.checkoutpage import CheckoutPage


class CartPage(BasePage):

    product = namedtuple('Product', ['name', 'total'])

    def __init__(self, driver):

        self.driver = driver

    # return a list of tuples with product name and its total amount
    def get_products(self):

        rows = self.get_rows()
        products = []
        for row in rows:
            name = row.find_element(*CartPageLocators.PRODUCT_NAME_IN_ROW).text
            product_total_text = str(row.find_element(*CartPageLocators.PRODUCT_TOTAL_IN_ROW).text)
            product_total_text = product_total_text.replace(ShopData.CURRENCY, "")
            total = float(product_total_text)
            products.append(self.product(name, total))
        return products

    def get_rows(self):

        return self.driver.find_elements(*CartPageLocators.PRODUCT_ROWS)

    def get_total(self):
        total_text = self.driver.find_element(*CartPageLocators.SUM_OF_TOTAL).text
        total_text = total_text.replace(ShopData.CURRENCY, "")
        return float(total_text)

    def click_checkout_button(self):

        self.click(CartPageLocators.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)
