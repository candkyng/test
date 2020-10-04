from pages.homepage import Homepage
from testfrwk.base_class import BaseClass


class TestPhoneShop(BaseClass):

    def test_e2e(self):
        # Test Data
        products_to_buy = ["Samsung Note 8", "Blackberry"]
        search_destination = "State"
        ship_to_destination = "United States of America"
        success_message_expected = "Success! Thank you! Your order will be delivered in next few weeks :-)."

        # Steps and Assertions
        product_page = Homepage(self.driver).click_shop_button()
        product_page.add_products_to_cart(products_to_buy)
        cart_page = product_page.click_checkout_button()
        products_in_cart = cart_page.get_products()
        product_names_in_cart = [p.name for p in products_in_cart]
        assert product_names_in_cart == products_to_buy

        product_totals_in_cart = [p.total for p in products_in_cart]
        assert sum(product_totals_in_cart) == cart_page.get_total()

        checkout_page = cart_page.click_checkout_button()
        checkout_page.enter_destination(search_destination)
        checkout_page.select_destination_from_dropdown(ship_to_destination)
        assert ship_to_destination == checkout_page.get_destination()

        checkout_page.click_agree_condition()
        checkout_page.click_purchase_button()
        assert success_message_expected in checkout_page.get_success_text()
