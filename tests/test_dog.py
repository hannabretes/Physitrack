import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.select_country_page import SelectCountryPage
from utils.conftest import driver
from utils.conftest import login_page


def test_page_load(driver):
    print("First testcase")
    #add_program = AddProgramPage(self.driver)
    #select_country = SelectCountryPage(self.driver)
    login_page.open("https://www.physitrack.co.uk/")
    login_page.click_login_button()
    #select_country.select_country_USA()
    login_page.click_back_to_demo()
    #add_program.add_to_card()

