from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class SelectCountryPage():
    country_usa_button = (By.ID, 'country_us')
    select_country_button = (By.XPATH, '//button[@name="button" and @class="btn-link pad-top choose-server" ]')
    def __init__(self, driver):
        super(SelectCountryPage, self).__init__(driver)

    def select_country_USA(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.do_click(self.country_usa_button)
        self.do_click(self.select_country_button)
