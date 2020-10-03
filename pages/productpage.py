from selenium.webdriver.common.by import By

from pages.cartpage import CartPage


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div[class='card h-100']")
    PRODUCT_NAME_IN_CARD = (By.CSS_SELECTOR, "div h4 a")
    PRODUCT_ADD_BUTTON_IN_CARD = (By.CSS_SELECTOR, "div button")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_products_to_cart(self, products_to_buy):

        product_cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        for card in product_cards:
            product_name_in_card = card.find_element(*self.PRODUCT_NAME_IN_CARD).text
            if product_name_in_card in products_to_buy:
                card.find_element(*self.PRODUCT_ADD_BUTTON_IN_CARD).click()

    def click_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return CartPage(self.driver)
