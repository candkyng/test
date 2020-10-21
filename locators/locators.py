from selenium.webdriver.common.by import By


class HomepageLocators:

    SHOP_BUTTON = (By.CSS_SELECTOR, "a[href*='shop']")
    HOME_BUTTON = (By.LINK_TEXT, "Home")
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    CHECKBOX_LOVE_ICE_CREAM = (By.ID, "exampleCheck1")
    GENDER_SELECT = (By.ID, "exampleFormControlSelect1")
    EMP_STATUS_STUDENT = (By.CSS_SELECTOR, "input[value='option1']")
    EMP_STATUS_EMPLOYED = (By.CSS_SELECTOR, "input[value='option2']")
    EMP_STATUS_ENTREPRENEUR = (By.CSS_SELECTOR, "input[value='option3']")
    DOB_FIELD = (By.NAME, "bday")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[value='Submit']")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(@class,'alert-success')]")


class CartPageLocators:

    PRODUCT_ROWS = (By.XPATH, "//td[contains(@class,'col-sm-8')]/parent::tr")
    PRODUCT_NAME_IN_ROW = (By.CSS_SELECTOR, "h4 a")
    PRODUCT_TOTAL_IN_ROW = (By.XPATH, "td[4]/strong")
    SUM_OF_TOTAL = (By.XPATH, "//td[@class='text-right']/h3/strong")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[class*='btn-success']")


class ProductPageLocators:

    PRODUCT_CARDS = (By.CSS_SELECTOR, "div[class='card h-100']")
    PRODUCT_NAME_IN_CARD = (By.CSS_SELECTOR, "div h4 a")
    PRODUCT_ADD_BUTTON_IN_CARD = (By.CSS_SELECTOR, "div button")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a[class*='btn-primary']")


class CheckoutPageLocators:

    COUNTRY_INPUT = (By.ID, "country")
    AGREE_CONDITION = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary'")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "input[value='Purchase']")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div[class*='alert-success']")