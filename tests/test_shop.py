from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.cartpage import CartPage
from pages.homepage import Homepage
from pages.productpage import ProductPage
from testfrwk.base_class import BaseClass


class TestPhoneShop(BaseClass):

    def test_e2e(self):

        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_shop_button()
        products_to_buy = ["Samsung Note 8", "Blackberry"]
        currency = "₹. "
        ship_to_destination = "United States of America"
        success_message_expected = "Success! Thank you! Your order will be delivered in next few weeks :-)."

        product_page = ProductPage(driver)
        product_page.add_products_to_cart(products_to_buy)
        product_page.click_checkout_button()

        cart_page = CartPage(driver)
        products_in_cart = cart_page.get_products()
        product_names_in_cart = [p.name for p in products_in_cart]
        assert product_names_in_cart == products_to_buy

        product_totals_in_cart = [p.total for p in products_in_cart]
        assert sum(product_totals_in_cart) == cart_page.get_total()

        cart_page.click_checkout_button()

        driver.find_element_by_id("country").send_keys("United")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[class='suggestions']")))

        ship_to_destination_xpath = "//a[text()='" + ship_to_destination + "']"
        driver.find_element_by_xpath(ship_to_destination_xpath).click()
        driver.find_element_by_css_selector("div[class='checkbox checkbox-primary'").click()
        driver.find_element_by_css_selector("input[value='Purchase']").click()
        success_text = driver.find_element_by_css_selector("div[class*='alert-success']").text
        assert success_message_expected in success_text
