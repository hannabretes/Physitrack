from Physitrack.utils.locators import MainPageLocators
from Physitrack.pages.base_page import BasePage

class SelectCountryPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(SelectCountryPage, self).__init__(driver)

    def select_country_USA(self):
        self.find_element(*self.locator.COUNTRY_USA).click()
        self.find_element(*self.locator.SELECT_COUNTRY).click()