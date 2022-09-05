import pytest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    login = (By.XPATH, '//a[@class="button-secondary button-small margin-left w-button"]')
    back_to_demo_button = (By.CLASS_NAME, 'link-back-to-demo')
    def click_login_button(self):
        self.do_click(self.login)

    def click_back_to_demo(self):
        self.do_click(self.back_to_demo_button)
