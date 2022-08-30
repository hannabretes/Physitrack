from utils.locators import MainPageLocators
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
class AddProgramPage(BasePage):
    CLOSE_POPUP = (By.XPATH, '//div[contains(@class, "current")]//a[@rel="modal:close"]')
    ADD_TO_CARD_BUTTON = (By.XPATH, '//button[@class="cart w-inline-block btn-link-icon pad-left "]')
    ASSIGN_PROGRAM = (By.ID, 'assign-program-modal-button')
    SELECT_PROGRAM = (By.CLASS_NAME, 'react-select__value-container css-1hwfws3')
    SELECT_USER = (By.XPATH, '//span[@class="ladda-label"]')
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(AddProgramPage, self).__init__(driver)
    def add_to_card(self):
        page = BasePage(self.driver)
        #page.do_click(self.CLOSE_POPUP)
        #self.driver.execute_script("arguments[0].click();", self.CLOSE_POPUP)
        #self.do_click(self.locator.CLOSE_POPUP).click()
        self.do_click(self.locator.BIRD_DOG_EXERCISE)
        self.do_click(self.locator.ADD_TO_CARD_BUTTON)