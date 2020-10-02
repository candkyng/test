from collections import namedtuple

from selenium.webdriver.common.by import By

from pages.checkoutpage import CheckoutPage


class CartPage:

    # Locators
    product_rows = (By.XPATH, "//td[contains(@class,'col-sm-8')]/parent::tr")
    product_name_in_row = (By.CSS_SELECTOR, "h4 a")
    product_total_in_row = (By.XPATH, "td[4]/strong")
    sum_of_total = (By.XPATH, "//td[@class='text-right']/h3/strong")
    checkout_button = (By.CSS_SELECTOR, "button[class*='btn-success']")

    product = namedtuple('Product', ['name', 'total'])
    currency = "₹. "

    def __init__(self, driver):

        self.driver = driver

    # return a list of tuples with product name and its total amount
    def get_products(self):

        rows = self.get_rows()
        products = []
        for row in rows:
            name = row.find_element(*CartPage.product_name_in_row).text
            product_total_text = str(row.find_element(*CartPage.product_total_in_row).text)
            product_total_text = product_total_text.replace(CartPage.currency, "")
            total = float(product_total_text)
            products.append(self.product(name, total))
        return products

    def get_rows(self):

        return self.driver.find_elements(*CartPage.product_rows)

    def get_total(self):
        total_text = self.driver.find_element(*CartPage.sum_of_total).text
        total_text = total_text.replace(CartPage.currency, "")
        return float(total_text)

    def click_checkout_button(self):

        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)