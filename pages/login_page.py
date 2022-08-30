from utils.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    LOGIN = (By.XPATH, '//a[@class="button-secondary button-small margin-left w-button"]')
    BACK_TO_DEMO_BUTTON = (By.CLASS_NAME, 'link-back-to-demo')
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(LoginPage, self).__init__(driver)

    def click_login_button(self):
        self.do_click(self.LOGIN)

    def click_back_to_demo(self):
        self.do_click(self.BACK_TO_DEMO_BUTTON)