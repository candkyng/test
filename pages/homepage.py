from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    loc_shop_button = (By.CSS_SELECTOR, "a[href*='shop']")

    # Objects
    def click_shop_button(self):

        self.driver.find_element(*self.loc_shop_button).click()
