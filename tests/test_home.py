import pytest

from data.home_data import HomeData
from locators.locators import HomepageLocators
from pages.homepage import Homepage
from testutil.base_class import BaseClass
from datetime import datetime


class TestHomepage(BaseClass):

    def test_home(self, home_data):
        log = self.get_logger()
        self.log_testdata_info(log, home_data)
        homepage = Homepage(self.driver, self.test_url)
        homepage.goto()
        homepage.enter_name(home_data['name'])
        homepage.enter_email(home_data['email'])
        homepage.enter_password(home_data['password'])
        homepage.select_love_ice_cream(home_data['love_ice_cream'])
        homepage.select_gender(home_data['gender'])
        homepage.select_employment_status(home_data['status'])
        homepage.enter_date_of_birth(home_data['birthdate'])
        homepage.click_submit_button()
        # Verify data is shown on the UI
        assert homepage.get_text_from_input(HomepageLocators.NAME_FIELD) == home_data['name']
        assert homepage.get_text_from_input(HomepageLocators.EMAIL_FIELD) == home_data['email']
        assert homepage.get_love_ice_cream() == home_data['love_ice_cream']
        assert homepage.get_text_from_input(HomepageLocators.GENDER_SELECT) == home_data['gender']
        assert homepage.get_employment_status() == home_data['status']
        assert homepage.get_text_from_input(HomepageLocators.DOB_FIELD) == home_data['birthdate'].strftime('%Y-%m-%d')
        assert HomeData.SUCCESS_TEXT_EXPECTED in homepage.get_success_text()

    @pytest.fixture(params=HomeData.get_list_all_data())
    def home_data(self, request):
        return request.param
