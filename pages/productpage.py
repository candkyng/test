from locators.locators import ProductPageLocators
from pages.basepage import BasePage
from pages.cartpage import CartPage


class ProductPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, products_to_buy):

        product_cards = self.driver.find_elements(*ProductPageLocators.PRODUCT_CARDS)
        for card in product_cards:
            product_name_in_card = card.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CARD).text
            if product_name_in_card in products_to_buy:
                self.click(ProductPageLocators.PRODUCT_ADD_BUTTON_IN_CARD, card)

    # Get the number found in checkout button
    def get_checkout_number(self):
        checkout_button_text = str(self.driver.find_element(*ProductPageLocators.CHECKOUT_BUTTON).text)
        #print("checkout_button_text:" + checkout_button_text)
        number = checkout_button_text.split(" ")[2]
        return int(number)

    def click_checkout_button(self):
        self.click(ProductPageLocators.CHECKOUT_BUTTON)
        return CartPage(self.driver)
