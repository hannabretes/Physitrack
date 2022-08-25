from Physitrack.utils.locators import MainPageLocators
from Physitrack.pages.base_page import BasePage
from selenium.webdriver.common.by import By
class SelectCountryPage(BasePage):
    COUNTRY_USA = (By.ID, 'country_us')
    SELECT_COUNTRY = (By.XPATH, '//button[@name="button" and @class="btn-link pad-top choose-server" ]')
    def __init__(self, driver):
        super(SelectCountryPage, self).__init__(driver)


    def select_country_USA(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.do_click(self.COUNTRY_USA)
        self.do_click(self.SELECT_COUNTRY)