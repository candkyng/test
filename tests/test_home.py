import pytest

from data.home_data import HomeData
from pages.homepage import Homepage
from testutil.base_class import BaseClass


class TestHomepage(BaseClass):

    def test_home(self, home_data):
        homepage = Homepage(self.driver)
        homepage.goto()
        homepage.enter_name(home_data['name'])
        homepage.enter_email(home_data['email'])
        homepage.enter_password(home_data['password'])
        homepage.select_love_ice_cream(home_data['love_ice_cream'])
        homepage.select_gender(home_data['gender'])
        homepage.select_employment_status(home_data['status'])
        homepage.enter_date_of_birth(home_data['birthdate'])
        homepage.click_submit_button()
        assert HomeData.SUCCESS_TEXT_EXPECTED in homepage.get_success_text()

    @pytest.fixture(params=HomeData.HOMETEST)
    def home_data(self, request):
        return request.param
