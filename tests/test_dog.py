import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.select_country_page import SelectCountryPage
from utils.conftest import BaseTest
from pages.add_program_page import AddProgramPage
@pytest.mark.usefixtures("setup")
class TestDog(BaseTest):
    def test_page_load(self):
        print("First testcase")
        page = BasePage(self.driver)
        login = LoginPage(self.driver)
        add_program = AddProgramPage(self.driver)
        select_country = SelectCountryPage(self.driver)
        page.open("https://www.physitrack.co.uk/")
        login.click_login_button()
        select_country.select_country_USA()
        login.click_back_to_demo()
        add_program.add_to_card()

