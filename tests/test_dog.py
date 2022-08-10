import pytest
from Physitrack.pages.base_page import BasePage
from Physitrack.pages.login_page import LoginPage
from Physitrack.pages.select_country_page import SelectCountryPage
from Physitrack.tests.base_test import BaseTest


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestDog(BaseTest):

    def test_page_load(self):
        page = BasePage(self.driver)
        page.open("https://www.physitrack.co.uk/")

