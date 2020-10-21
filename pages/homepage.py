from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from locators.locators import HomepageLocators
from pages.basepage import BasePage
from pages.productpage import ProductPage


class Homepage(BasePage):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def goto(self):
        self.driver.get(self.url)
        return self

    def click_home_button(self):
        self.click(HomepageLocators.HOME_BUTTON)
        return self

    def click_shop_button(self):
        self.click(HomepageLocators.SHOP_BUTTON)
        return ProductPage(self.driver)

    def enter_name(self, name):
        self.enter_text(HomepageLocators.NAME_FIELD, name)

    def enter_email(self, email):
        self.enter_text(HomepageLocators.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.enter_text(HomepageLocators.PASSWORD_FIELD, password)

    def select_love_ice_cream(self, selection):
        check_status = self.get_love_ice_cream()
        if selection is not check_status:
            self.click(HomepageLocators.CHECKBOX_LOVE_ICE_CREAM)

    def select_gender(self, selection):
        gender = Select(self.driver.find_element(*HomepageLocators.GENDER_SELECT))
        gender.select_by_visible_text(selection)

    def select_employment_status(self, selection):
        if selection == 'student':
            self.click(HomepageLocators.EMP_STATUS_STUDENT)
        elif selection == 'employed':
            self.click(HomepageLocators.EMP_STATUS_EMPLOYED)

    def enter_date_of_birth(self, date):
        '''
        Enter date of birth
        :param date: datetime object
        :return:
        '''
        dob_input = date.strftime('%m%d%Y')  # convert to string format
        bday = self.driver.find_element(*HomepageLocators.DOB_FIELD)
        bday.click()
        ActionChains(self.driver).send_keys_to_element(bday, dob_input).perform()

    def click_submit_button(self):
        self.click(HomepageLocators.SUBMIT_BUTTON)

    def get_success_text(self):
        return self.driver.find_element(*HomepageLocators.SUCCESS_TEXT).text

    def get_employment_status(self):
        if self.driver.find_element(*HomepageLocators.EMP_STATUS_STUDENT).is_selected() is True:
            return 'student'
        elif self.driver.find_element(*HomepageLocators.EMP_STATUS_EMPLOYED).is_selected() is True:
            return 'employed'
        return None

    def get_love_ice_cream(self):
        return self.driver.find_element(*HomepageLocators.CHECKBOX_LOVE_ICE_CREAM).is_selected()
