from Physitrack.utils.locators import MainPageLocators
from Physitrack.pages.base_page import BasePage

class AddProgramPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(AddProgramPage, self).__init__(driver)

    def click_add_to_card(self):
        page = BasePage(self.driver)
        page.wait_element(*self.locator.CLOSE_POPUP)
        self.find_element(*self.locator.CLOSE_POPUP).click()
        self.find_element(*self.locator.BIRD_DOG_EXERCISE).click()
        self.find_element(*self.locator.ADD_TO_CARD_BUTTON).click()