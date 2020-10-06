from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.cartpage import CartPage


class ProductPage(BasePage):

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
                self.click(self.PRODUCT_ADD_BUTTON_IN_CARD, card)

    # Get the number found in checkout button
    def get_checkout_number(self):
        checkout_button_text = str(self.driver.find_element(*self.CHECKOUT_BUTTON).text)
        #print("checkout_button_text:" + checkout_button_text)
        number = checkout_button_text.split(" ")[2]
        return int(number)

    def click_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)
        return CartPage(self.driver)
