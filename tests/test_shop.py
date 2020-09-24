from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestPhoneShop:

    def test_e2e(self):

        base_url = "https://rahulshettyacademy.com/angularpractice/"

        driver = webdriver.Chrome(executable_path="C:\\Users\\candk\\Envs\\amazon\\Scripts\\chromedriver.exe")
        driver.get(base_url)
        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.find_element_by_css_selector("a[href*='shop']").click()
        products_to_buy = ["Samsung Note 8"]
        currency = "₹. "
        ship_to_destination = "United States of America"
        success_message_expected = "Success! Thank you! Your order will be delivered in next few weeks :-)."

        e_products = driver.find_elements_by_css_selector("div[class='card h-100']")
        print(len(e_products))
        for eProduct in e_products:
            product_name = eProduct.find_element_by_css_selector("div h4 a").text
            print(product_name)
            if product_name in products_to_buy:
                eProduct.find_element_by_css_selector("div button").click()

        driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        e_products_in_cart = driver.find_elements_by_xpath("//td[contains(@class,'col-sm-8')]/parent::tr")
        total = 0
        for eProduct in e_products_in_cart:
            product_name_in_cart = eProduct.find_element_by_css_selector("h4 a").text
            print(product_name_in_cart)
            assert product_name_in_cart in products_to_buy
            product_total_text = str(eProduct.find_element_by_xpath("td[4]/strong").text)
            product_total_text = product_total_text.replace(currency, "")
            total += float(product_total_text)

        total_expected_text = driver.find_element_by_xpath("//td[@class='text-right']/h3/strong").text
        print(total_expected_text)
        total_expected_text = total_expected_text.replace(currency, "")
        print(total_expected_text)
        total_expected = float(total_expected_text)
        assert total == total_expected

        driver.find_element_by_css_selector("button[class*='btn-success']").click()
        driver.find_element_by_id("country").send_keys("United")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[class='suggestions']")))

        ship_to_destination_xpath = "//a[text()='" + ship_to_destination + "']"
        driver.find_element_by_xpath(ship_to_destination_xpath).click()
        driver.find_element_by_css_selector("div[class='checkbox checkbox-primary'").click()
        driver.find_element_by_css_selector("input[value='Purchase']").click()
        success_text = driver.find_element_by_css_selector("div[class*='alert-success']").text
        assert success_message_expected in success_text
