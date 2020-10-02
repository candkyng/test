from selenium.webdriver.common.by import By

from pages.cartpage import CartPage


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    product_cards = (By.CSS_SELECTOR, "div[class='card h-100']")
    product_name_in_card = (By.CSS_SELECTOR, "div h4 a")
    product_add_button_in_card = (By.CSS_SELECTOR, "div button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_products_to_cart(self, products_to_buy):

        product_cards = self.driver.find_elements(*self.product_cards)
        for card in product_cards:
            product_name_in_card = card.find_element(*self.product_name_in_card).text
            if product_name_in_card in products_to_buy:
                card.find_element(*self.product_add_button_in_card).click()

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()
        return CartPage(self.driver)
