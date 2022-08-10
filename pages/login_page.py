from Physitrack.utils.locators import MainPageLocators
from Physitrack.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(LoginPage, self).__init__(driver)

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN).click()
    def click_back_to_demo(self):
        self.find_element(*self.locator.BACK_TO_DEMO_BUTTON).click()